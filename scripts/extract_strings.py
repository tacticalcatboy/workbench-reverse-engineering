#!/usr/bin/env python3
"""Extract diagnostic-related strings from Workbench executable."""

import re
import os

def extract_strings(filename, min_length=8):
    """Extract ASCII and Unicode strings from binary file."""
    with open(filename, 'rb') as f:
        data = f.read()

    # Find ASCII strings
    ascii_pattern = rb'[\x20-\x7e]{' + str(min_length).encode() + rb',}'
    ascii_strings = re.findall(ascii_pattern, data)

    # Find Unicode (UTF-16LE) strings - common in Windows binaries
    unicode_strings = []
    unicode_pattern = rb'(?:[\x20-\x7e]\x00){' + str(min_length).encode() + rb',}'
    unicode_matches = re.findall(unicode_pattern, data)
    for match in unicode_matches:
        try:
            decoded = match.decode('utf-16-le')
            if len(decoded) >= min_length:
                unicode_strings.append(decoded)
        except:
            pass

    all_strings = [s.decode('ascii', errors='ignore') for s in ascii_strings]
    all_strings.extend(unicode_strings)

    return list(set(all_strings))

def main():
    exe_path = r"D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\ArmaReforgerWorkbenchSteamDiag.exe"
    output_dir = r"C:\Users\scarlett\Documents\workbench-reverse-engineering"

    print(f"Extracting strings from: {exe_path}")
    print("=" * 80)

    strings = extract_strings(exe_path, min_length=8)
    print(f"Total strings found: {len(strings)}")

    # Diagnostic-related keywords to search for
    diagnostic_keywords = [
        'is not used',
        'not used',
        'obsolete',
        'deprecated',
        'conflict',
        'can be const',
        'could be const',
        'No need to use',
        'Cast',
        'warning',
        'Warning',
        'WARN',
        'error',
        'Error',
        'ERROR',
        'hint',
        'Hint',
        'Variable',
        'variable',
        'overwrites',
        'ResourceName',
        'picker',
        'up-cast',
        'upcast',
        'script default value',
        'Possible variable',
        'shadowing',
        'shadow',
        'unused',
        'unreachable',
        'redundant',
    ]

    # Collect diagnostic-like strings
    found = set()
    skip_patterns = ['http', 'www.', '.dll', '.exe', 'copyright', '(c)', 'license',
                     'microsoft', 'windows', '<', '>', '{', '}', '\\', '//', '/*',
                     'MSVC', 'Visual Studio', 'Qt', 'opencv', 'opengl']

    for s in strings:
        s_lower = s.lower()
        # Check if contains diagnostic keyword
        for kw in diagnostic_keywords:
            if kw.lower() in s_lower:
                # Filter out obvious non-diagnostic strings
                skip = False
                for sp in skip_patterns:
                    if sp.lower() in s_lower:
                        skip = True
                        break
                if not skip and 15 < len(s) < 300:
                    found.add(s.strip())
                break

    # Write all strings to file
    all_file = os.path.join(output_dir, 'all_strings.txt')
    with open(all_file, 'w', encoding='utf-8') as f:
        for s in sorted(strings):
            if len(s) > 10:
                f.write(s + '\n')
    print(f"All strings written to: {all_file}")

    # Write diagnostic strings
    diag_file = os.path.join(output_dir, 'diagnostic_strings.txt')
    with open(diag_file, 'w', encoding='utf-8') as f:
        f.write("=== DIAGNOSTIC-RELATED STRINGS FROM WORKBENCH ===\n")
        f.write(f"Total strings scanned: {len(strings)}\n")
        f.write(f"Diagnostic strings found: {len(found)}\n")
        f.write("=" * 50 + "\n\n")
        for s in sorted(found):
            f.write(s + '\n')
    print(f"Diagnostic strings written to: {diag_file}")

    # Print diagnostic strings
    print("\n" + "=" * 80)
    print("=== DIAGNOSTIC-RELATED STRINGS ===")
    print("=" * 80 + "\n")
    for s in sorted(found):
        print(f"  {s}")

    print(f"\n\nTotal diagnostic strings: {len(found)}")

if __name__ == '__main__':
    main()
