# Enforce Script Tools

Tools and documentation for **Enforce Script** - the scripting language used in Bohemia Interactive's Enfusion engine (Arma Reforger).

## What This Is

This project provides:
- **Parser scripts** for extracting API documentation from your local game installation
- **Analysis tools** for understanding Enforce Script patterns
- **Documentation** about the language syntax, grammar, and compiler behavior

## Requirements

- **Arma Reforger** (Steam)
- **Arma Reforger Tools** (free DLC on Steam)
- **Python 3.8+** with `beautifulsoup4` and `lxml`

## Quick Start

### 1. Install Dependencies

```bash
# Python packages for parsing
pip install beautifulsoup4 lxml

# MkDocs for viewing documentation
pip install mkdocs mkdocs-material
```

### 2. Generate API Data

The API data must be generated locally from your game installation:

```bash
# Parse the official Doxygen API documentation
python scripts/parse_api_docs.py
```

This creates:
- `data/api/enfusion.json` - 824 Enfusion engine classes
- `data/api/arma-reforger.json` - 7,880 Arma Reforger classes
- `data/api/summary.json` - Quick lookup data
- `data/api/inheritance-tree.json` - Class hierarchy

### 3. View Documentation

```bash
mkdocs serve
# Open http://localhost:8000
```

## Project Structure

```
enforce-script-tools/
├── docs/              # Language documentation (MkDocs)
├── scripts/           # Parser and analysis tools
│   └── parse_api_docs.py
├── data/              # Generated locally (gitignored)
│   └── api/           # Parsed API JSON files
├── prompts/           # AI assistant prompts
├── mkdocs.yml         # Documentation config
├── LICENSE            # MIT License
└── NOTICE             # Copyright notices
```

## Key Findings

From reverse engineering the Workbench compiler:

- **120+ diagnostic patterns** - Error and warning messages
- **19 AST node types** - Internal compiler representation
- **1,833 ClassRegistrator entries** - Registered script classes
- **7 log levels** - Fatal, Error, Warning, Normal, Verbose, Debug, Spam

## Scripts

| Script | Purpose |
|--------|---------|
| `parse_api_docs.py` | Parse Doxygen HTML to JSON |
| `extract_strings.py` | Extract strings from binaries |

## Legal

This project contains **only tools and documentation**, not game content.

- Tools are MIT licensed (see [LICENSE](LICENSE))
- Game content belongs to Bohemia Interactive (see [NOTICE](NOTICE))
- Created for interoperability and modding education

## Contributing

Contributions welcome! Please ensure you don't commit:
- Extracted game data
- Binary files
- API JSON files (these are generated locally)

## Links

- [Arma Reforger Wiki](https://community.bistudio.com/wiki/Arma_Reforger)
- [Enfusion Workbench](https://community.bistudio.com/wiki/Arma_Reforger:Enfusion_Workbench)
- [Bohemia Interactive Forums](https://forums.bohemia.net/)
