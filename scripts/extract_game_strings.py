#!/usr/bin/env python3
"""Extract strings from Arma Reforger game executable and compare with Workbench."""

import re
import os

def extract_strings(filename, min_length=8):
    """Extract ASCII and Unicode strings from binary file."""
    with open(filename, 'rb') as f:
        data = f.read()

    # Find ASCII strings
    ascii_pattern = rb'[\x20-\x7e]{' + str(min_length).encode() + rb',}'
    ascii_strings = re.findall(ascii_pattern, data)

    # Find Unicode (UTF-16LE) strings
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
    game_exe = r"D:\SteamLibrary\steamapps\common\Arma Reforger\ArmaReforgerSteamDiag.exe"
    output_dir = r"C:\Users\scarlett\Documents\workbench-reverse-engineering"

    print(f"Extracting strings from GAME: {game_exe}")
    print("=" * 80)

    game_strings = extract_strings(game_exe, min_length=8)
    print(f"Total strings found in game: {len(game_strings)}")

    # Write game strings
    game_file = os.path.join(output_dir, 'game_all_strings.txt')
    with open(game_file, 'w', encoding='utf-8') as f:
        for s in sorted(game_strings):
            if len(s) > 10:
                f.write(s + '\n')
    print(f"Game strings written to: {game_file}")

    # Load workbench strings for comparison
    workbench_file = os.path.join(output_dir, 'all_strings.txt')
    workbench_strings = set()
    if os.path.exists(workbench_file):
        with open(workbench_file, 'r', encoding='utf-8') as f:
            workbench_strings = set(line.strip() for line in f if line.strip())
        print(f"Loaded {len(workbench_strings)} strings from Workbench")

    game_set = set(s for s in game_strings if len(s) > 10)

    # Find differences
    game_only = game_set - workbench_strings
    workbench_only = workbench_strings - game_set
    shared = game_set & workbench_strings

    print(f"\nComparison:")
    print(f"  Game only: {len(game_only)}")
    print(f"  Workbench only: {len(workbench_only)}")
    print(f"  Shared: {len(shared)}")

    # Write game-only strings (potential runtime errors)
    game_only_file = os.path.join(output_dir, 'game_only_strings.txt')
    with open(game_only_file, 'w', encoding='utf-8') as f:
        f.write(f"=== STRINGS UNIQUE TO GAME (Runtime) ===\n")
        f.write(f"Total: {len(game_only)}\n")
        f.write("=" * 50 + "\n\n")
        for s in sorted(game_only):
            f.write(s + '\n')
    print(f"Game-only strings written to: {game_only_file}")

    # Filter for diagnostic-like strings in game-only
    diagnostic_keywords = [
        'error', 'Error', 'ERROR', 'warning', 'Warning', 'WARN',
        'failed', 'Failed', 'FAILED', 'invalid', 'Invalid',
        'cannot', 'Cannot', "can't", "Can't",
        'missing', 'Missing', 'not found', 'Not found',
        'null', 'NULL', 'nullptr',
        'exception', 'Exception', 'crash', 'Crash',
        'script', 'Script', 'RPC', 'replication', 'Replication'
    ]

    game_diagnostics = []
    skip_patterns = ['http', 'www.', '.dll', '.exe', 'copyright', '(c)', 'license',
                     'microsoft', 'windows', '<', '>', '{', '}', '\\\\', '//', '/*']

    for s in game_only:
        s_lower = s.lower()
        for kw in diagnostic_keywords:
            if kw.lower() in s_lower:
                skip = False
                for sp in skip_patterns:
                    if sp.lower() in s_lower:
                        skip = True
                        break
                if not skip and 15 < len(s) < 300:
                    game_diagnostics.append(s)
                break

    # Write game-only diagnostics
    game_diag_file = os.path.join(output_dir, 'game_only_diagnostics.txt')
    with open(game_diag_file, 'w', encoding='utf-8') as f:
        f.write(f"=== DIAGNOSTIC STRINGS UNIQUE TO GAME ===\n")
        f.write(f"These are likely RUNTIME errors not in Workbench\n")
        f.write(f"Total: {len(game_diagnostics)}\n")
        f.write("=" * 50 + "\n\n")
        for s in sorted(game_diagnostics):
            f.write(s + '\n')
    print(f"Game-only diagnostics written to: {game_diag_file}")
    print(f"Found {len(game_diagnostics)} potential runtime diagnostic strings")

if __name__ == '__main__':
    main()
