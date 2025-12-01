# Setup Guide

How to set up the reverse engineering environment.

## Prerequisites

### Required Software

1. **JDK 21+** - Required for Ghidra
   - Download: [Eclipse Adoptium](https://adoptium.net/)
   - Verify: `java -version`

2. **Ghidra 11.4.2** - Reverse engineering tool
   - Already included in `tools/ghidra_11.4.2_PUBLIC/`
   - Or download from [ghidra-sre.org](https://ghidra-sre.org/)

3. **Python 3.x** - For extraction scripts
   - Download: [python.org](https://www.python.org/)

## Workbench Location

The target binary is located at:

```
D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\
```

**Primary binary:** `ArmaReforgerWorkbenchSteamDiag.exe` (v1.6.0.76, ~67MB)

**Game binary:** `ArmaReforgerSteamDiag.exe` (for runtime error comparison)

## Running Ghidra

1. Navigate to `tools/ghidra_11.4.2_PUBLIC/`
2. Run `ghidraRun.bat` (Windows) or `ghidraRun` (Linux/Mac)
3. Open the existing project: `tools/WorkbenchAnalysis.gpr`

## String Extraction

### Using Python Scripts

Extract strings from Workbench:
```bash
python scripts/extract_strings.py
```

Extract and compare game strings:
```bash
python scripts/extract_game_strings.py
```

### Using Ghidra

1. Open the binary in Ghidra
2. Let auto-analysis complete
3. Go to **Window > Defined Strings**
4. Export via **File > Export** or use the Java script

## Output Files

| File | Location | Description |
|------|----------|-------------|
| `all_strings.txt` | `data/workbench/` | All Workbench strings (84,718) |
| `diagnostic_strings.txt` | `data/workbench/` | Filtered diagnostics |
| `game_all_strings.txt` | `data/game/` | All game strings (61,575) |
| `game_only_strings.txt` | `data/game/` | Strings unique to game |
| `game_only_diagnostics.txt` | `data/game/` | Runtime-only diagnostics |

## Searching Strings

### Using grep

```bash
# Find error patterns
grep -i "error" data/workbench/all_strings.txt

# Find specific patterns
grep "'%s'" data/workbench/all_strings.txt | grep -i "cannot"

# Find class names
grep "Registrator" data/workbench/all_strings.txt
```

### Pattern Tips

- `%s` - String placeholder
- `%d` - Integer placeholder
- `@enf` - Engine namespace
- `@gamelib` - Game library namespace
- `@gamecode` - Game-specific namespace
