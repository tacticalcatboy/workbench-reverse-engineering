#!/usr/bin/env python3
"""
Parse Doxygen HTML documentation into structured JSON for AI consumption.

This script parses the Enfusion and Arma Reforger API documentation from
Doxygen HTML files and outputs structured JSON files.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup, Tag


def parse_type_from_html(td: Tag) -> str:
    """Extract type from a table cell, handling links and special characters."""
    if td is None:
        return ""

    # Get text content, preserving spaces around links
    parts = []
    for child in td.children:
        if isinstance(child, Tag):
            if child.name == 'a':
                parts.append(child.get_text(strip=True))
            else:
                parts.append(child.get_text(strip=True))
        else:
            text = str(child).strip()
            if text:
                parts.append(text)

    result = ' '.join(parts)
    # Clean up extra whitespace
    result = re.sub(r'\s+', ' ', result).strip()
    # Remove "proto external" prefix
    result = re.sub(r'^proto\s+external\s+', '', result)
    result = re.sub(r'^proto\s+', '', result)
    result = re.sub(r'^external\s+', '', result)
    return result


def parse_method_signature(method_row: Tag, desc_row: Optional[Tag]) -> dict:
    """Parse a method from its table row."""
    method = {
        "name": "",
        "returnType": "void",
        "parameters": [],
        "static": False,
        "access": "public",
        "description": ""
    }

    # Get return type from left column
    left_td = method_row.find('td', class_='memItemLeft')
    if left_td:
        return_type = parse_type_from_html(left_td)
        if 'static' in return_type.lower():
            method['static'] = True
            return_type = re.sub(r'static\s+', '', return_type, flags=re.IGNORECASE)
        method['returnType'] = return_type.strip() or 'void'

    # Get method name and parameters from right column
    right_td = method_row.find('td', class_='memItemRight')
    if right_td:
        # Get method name from the anchor
        method_link = right_td.find('a', class_='el')
        if method_link:
            method['name'] = method_link.get_text(strip=True)

        # Get full text for parameter parsing
        full_text = right_td.get_text()

        # Extract parameters from parentheses
        param_match = re.search(r'\(([^)]*)\)', full_text)
        if param_match:
            params_str = param_match.group(1).strip()
            if params_str:
                method['parameters'] = parse_parameters(params_str)

    # Get description from description row
    if desc_row:
        desc_td = desc_row.find('td', class_='mdescRight')
        if desc_td:
            method['description'] = desc_td.get_text(strip=True)

    return method


def parse_parameters(params_str: str) -> list:
    """Parse parameter string into list of parameter objects."""
    params = []
    if not params_str or params_str.isspace():
        return params

    # Split by comma, but be careful of nested types like array<T>
    depth = 0
    current = ""
    parts = []

    for char in params_str:
        if char in '<[(':
            depth += 1
            current += char
        elif char in '>])':
            depth -= 1
            current += char
        elif char == ',' and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += char

    if current.strip():
        parts.append(current.strip())

    for part in parts:
        part = part.strip()
        if not part:
            continue

        param = {"name": "", "type": ""}

        # Handle default values
        if '=' in part:
            part = part.split('=')[0].strip()

        # Handle modifiers like 'out', 'inout', 'notnull', 'const'
        modifiers = []
        for mod in ['out', 'inout', 'notnull', 'const']:
            if part.startswith(mod + ' '):
                modifiers.append(mod)
                part = part[len(mod):].strip()

        # Split type and name - name is last token
        tokens = part.split()
        if len(tokens) >= 2:
            param['name'] = tokens[-1]
            param['type'] = ' '.join(tokens[:-1])
        elif len(tokens) == 1:
            # Just a type with no name (like in callbacks)
            param['type'] = tokens[0]
            param['name'] = ""

        if modifiers:
            param['modifiers'] = modifiers

        params.append(param)

    return params


def parse_class_file(filepath: Path) -> Optional[dict]:
    """Parse a single class HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(content, 'lxml')

    # Get class name from title
    title = soup.find('title')
    if not title:
        return None

    title_text = title.get_text()
    # Extract class name from title like "Enfusion Script API: BaseWorld Interface Reference"
    name_match = re.search(r':\s*(\S+)\s+(?:Interface|Class|Struct)', title_text)
    if name_match:
        class_name = name_match.group(1)
    else:
        # Fallback: try to get from headertitle
        header = soup.find('div', class_='headertitle')
        if header:
            header_text = header.get_text()
            name_match = re.search(r'^(\S+)', header_text.strip())
            if name_match:
                class_name = name_match.group(1)
            else:
                return None
        else:
            return None

    class_data = {
        "name": class_name,
        "extends": None,
        "module": "",
        "methods": [],
        "properties": [],
        "description": ""
    }

    # Get module/group from ingroups
    ingroups = soup.find('div', class_='ingroups')
    if ingroups:
        group_link = ingroups.find('a')
        if group_link:
            class_data['module'] = group_link.get_text(strip=True)

    # Get inheritance from the inheritance diagram map
    # Look for parent classes (those that point to this class)
    inheritance_map = soup.find('map')
    if inheritance_map:
        areas = inheritance_map.find_all('area')
        # Find direct parent - typically the one just above in the hierarchy
        # We look for classes that are immediate parents
        for area in areas:
            href = area.get('href', '')
            alt = area.get('alt', '')
            # Skip self-references and derived classes
            if alt and alt != class_name:
                # Check if this is a parent by looking at coords
                # In Doxygen diagrams, parents are typically above (lower y coords)
                # For simplicity, we'll take the first non-self class as parent
                # unless it's clearly a child (World derives from BaseWorld)
                pass

        # Better approach: parse the text description if available
        inherit_text = soup.find(string=re.compile(r'Inheritance diagram'))
        if inherit_text:
            parent = inherit_text.find_parent()

    # Alternative: Look for "inherits from" text or inherited members section
    inherited_header = soup.find(string=re.compile(r'inherited from'))
    if inherited_header:
        parent_link = inherited_header.find_parent().find('a')
        if parent_link:
            class_data['extends'] = parent_link.get_text(strip=True)
    else:
        # Check inheritance from area map - find the base class
        if inheritance_map:
            areas = inheritance_map.find_all('area')
            # The inheritance diagram shows: parent at top, current in middle, children at bottom
            # Look for class that is "global_pointer" or "pointer" pattern for base types
            for area in areas:
                alt = area.get('alt', '')
                if alt and alt != class_name and 'pointer' not in alt.lower():
                    # This might be a parent - we need more context
                    # Check if there are inherited methods from this class
                    inherit_section = soup.find('td', string=re.compile(f'inherited from.*{re.escape(alt)}', re.IGNORECASE))
                    if inherit_section:
                        class_data['extends'] = alt
                        break

    # Parse methods from member declaration tables
    methods = []
    member_tables = soup.find_all('table', class_='memberdecls')

    for table in member_tables:
        rows = table.find_all('tr')
        i = 0
        while i < len(rows):
            row = rows[i]

            # Check if this is a method row - class is like "memitem:xxxx"
            row_classes = row.get('class', [])
            is_memitem = any(c.startswith('memitem') for c in row_classes)
            if is_memitem:
                # Look for description row
                desc_row = None
                if i + 1 < len(rows):
                    next_row = rows[i + 1]
                    next_classes = next_row.get('class', [])
                    if any(c.startswith('memdesc') for c in next_classes):
                        desc_row = next_row

                method = parse_method_signature(row, desc_row)
                if method['name']:
                    # Check if it's static from the section header
                    prev_header = row.find_previous('h2')
                    if prev_header and 'Static' in prev_header.get_text():
                        method['static'] = True

                    methods.append(method)

            i += 1

    class_data['methods'] = methods

    # Get class description from brief description
    brief = soup.find('div', class_='textblock')
    if brief:
        class_data['description'] = brief.get_text(strip=True)[:500]  # Limit length

    return class_data


def parse_api_docs(docs_path: Path) -> list:
    """Parse all class documentation from a Doxygen docs folder."""
    classes = []

    # Find all interface*.html files (excluding -members.html)
    class_files = list(docs_path.glob('interface*.html'))
    class_files = [f for f in class_files if not f.name.endswith('-members.html')]

    print(f"Found {len(class_files)} class files in {docs_path}")

    for i, filepath in enumerate(class_files):
        if (i + 1) % 100 == 0:
            print(f"Processing {i + 1}/{len(class_files)}...")

        class_data = parse_class_file(filepath)
        if class_data:
            classes.append(class_data)

    return classes


def build_inheritance_tree(classes: list) -> dict:
    """Build inheritance tree from parsed classes."""
    tree = {
        "roots": [],  # Classes with no parent
        "children": {}  # parent -> [children]
    }

    class_names = {c['name'] for c in classes}

    for cls in classes:
        parent = cls.get('extends')
        if parent and parent in class_names:
            if parent not in tree['children']:
                tree['children'][parent] = []
            tree['children'][parent].append(cls['name'])
        else:
            tree['roots'].append(cls['name'])

    return tree


def generate_summary(classes: list) -> dict:
    """Generate summary statistics from parsed classes."""
    summary = {
        "total_classes": len(classes),
        "class_names": sorted([c['name'] for c in classes]),
        "modules": {},
        "method_counts": {}
    }

    for cls in classes:
        # Count by module
        module = cls.get('module') or 'Unknown'
        if module not in summary['modules']:
            summary['modules'][module] = 0
        summary['modules'][module] += 1

        # Method count per class
        summary['method_counts'][cls['name']] = len(cls.get('methods', []))

    return summary


def main():
    parser = argparse.ArgumentParser(description='Parse Doxygen API docs to JSON')
    parser.add_argument('--enfusion', type=str,
                       default=r'D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\docs\EnfusionScriptAPIPublic\EnfusionScriptAPIPublic',
                       help='Path to EnfusionScriptAPIPublic docs')
    parser.add_argument('--arma', type=str,
                       default=r'D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\docs\ArmaReforgerScriptAPIPublic\ArmaReforgerScriptAPIPublic',
                       help='Path to ArmaReforgerScriptAPIPublic docs')
    parser.add_argument('--output', type=str, default='data/api',
                       help='Output directory for JSON files')
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_classes = []

    # Parse Enfusion API
    enfusion_path = Path(args.enfusion)
    if enfusion_path.exists():
        print(f"\n=== Parsing Enfusion Script API ===")
        enfusion_classes = parse_api_docs(enfusion_path)
        print(f"Parsed {len(enfusion_classes)} classes from Enfusion API")

        # Save Enfusion JSON
        with open(output_dir / 'enfusion.json', 'w', encoding='utf-8') as f:
            json.dump(enfusion_classes, f, indent=2)
        print(f"Saved to {output_dir / 'enfusion.json'}")

        all_classes.extend(enfusion_classes)
    else:
        print(f"Warning: Enfusion docs not found at {enfusion_path}")

    # Parse Arma Reforger API
    arma_path = Path(args.arma)
    if arma_path.exists():
        print(f"\n=== Parsing Arma Reforger Script API ===")
        arma_classes = parse_api_docs(arma_path)
        print(f"Parsed {len(arma_classes)} classes from Arma Reforger API")

        # Save Arma Reforger JSON
        with open(output_dir / 'arma-reforger.json', 'w', encoding='utf-8') as f:
            json.dump(arma_classes, f, indent=2)
        print(f"Saved to {output_dir / 'arma-reforger.json'}")

        all_classes.extend(arma_classes)
    else:
        print(f"Warning: Arma Reforger docs not found at {arma_path}")

    # Generate summary
    print(f"\n=== Generating Summary ===")
    summary = generate_summary(all_classes)
    with open(output_dir / 'summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(f"Saved summary to {output_dir / 'summary.json'}")

    # Generate inheritance tree
    print(f"\n=== Generating Inheritance Tree ===")
    tree = build_inheritance_tree(all_classes)
    with open(output_dir / 'inheritance-tree.json', 'w', encoding='utf-8') as f:
        json.dump(tree, f, indent=2)
    print(f"Saved inheritance tree to {output_dir / 'inheritance-tree.json'}")

    # Print summary
    print(f"\n=== Summary ===")
    print(f"Total classes parsed: {len(all_classes)}")
    print(f"Modules found: {len(summary['modules'])}")
    print(f"Root classes (no parent): {len(tree['roots'])}")


if __name__ == '__main__':
    main()
