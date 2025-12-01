# Enforce Script Diagnostics

Reverse-engineered diagnostic patterns from Arma Reforger Workbench.

!!! warning "Private Project"
    This directory is **separate** for legal/licensing reasons. Do not commit decompiled code or binary analysis to public repos.

## Project Goal

Reverse-engineer the Arma Reforger Workbench to understand:

1. All diagnostic types (errors, warnings, hints)
2. API surface (classes, methods, properties)
3. Syntax/grammar rules

**Purpose:** Enable AI to write better Enforce Script code - NOT to replace Workbench.

## Quick Stats

| Metric | Count |
|--------|-------|
| Workbench strings extracted | 84,718 |
| Game strings extracted | 61,575 |
| Diagnostic patterns found | 270+ |
| AST node types discovered | 19 |
| ClassRegistrator entries | 1,833 |
| **Official API classes (Enfusion)** | 824 |
| **Official API classes (Arma Reforger)** | 7,880 |
| **Total documented API classes** | **8,704** |

## Data Sources

### 1. Binary String Extraction (Reverse Engineering)
- **Workbench exe:** 84,718 strings - Compiler error messages, internal APIs
- **Game exe:** 61,575 strings - Runtime errors, RPC methods
- Location: `data/workbench/`, `data/game/`

### 2. Official API Documentation (Doxygen)
- **EnfusionScriptAPIPublic:** 824 classes - Engine-level API (IEntity, Physics, etc.)
- **ArmaReforgerScriptAPIPublic:** 7,880 classes - Game-level API (Components, AI, etc.)
- Location: `D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\docs\`
- Contains: Full method signatures, parameter types, return types, documentation

## Project Structure

```
workbench-reverse-engineering/
├── docs/           # Documentation (this site)
├── data/           # Extracted string data
│   ├── workbench/  # Workbench exe strings
│   └── game/       # Game exe strings
├── scripts/        # Extraction scripts
└── tools/          # Ghidra and analysis files
```

## Key Findings

### Diagnostic Categories

- **Warnings** - Obsolete APIs, unused variables, cast warnings
- **Hints** - Const suggestions
- **Type Errors** - Cast, array, void type errors
- **Inheritance Errors** - Sealed, override, circular inheritance
- **Constructor Errors** - Serialization, private constructors
- **RPC/Replication Errors** - Network-related diagnostics
- **Syntax Errors** - Brackets, EOF, parsing errors

### Compiler Infrastructure

- `CCompiler@enf` - Main compiler class
- `CParser@enf` / `CScriptParser@enf` - Parsing
- `Tokenizer@enf` - Lexer
- 19 AST node types in `ast@enf` namespace

### Log Levels

| Level | Priority |
|-------|----------|
| Fatal | Highest |
| Error | High |
| Warning | Medium |
| Normal | Standard |
| Verbose | Low |
| Debug | Lower |
| Spam | Lowest |

## Getting Started

1. [Setup Guide](getting-started/setup.md) - Install Ghidra and configure environment
2. [Checklist](getting-started/checklist.md) - Track progress

## Browse Findings

- [Diagnostics](findings/diagnostics.md) - All 120+ diagnostic patterns
- [Runtime Errors](findings/runtime-errors.md) - Game-only runtime errors
- [Keywords](findings/keywords.md) - Discovered language keywords
- [Types](findings/types.md) - Built-in type system
- [API Surface](findings/api.md) - Exposed classes and methods

## Reference

- [AST Nodes](reference/ast-nodes.md) - Abstract syntax tree structure
- [Compiler](reference/compiler.md) - Compiler infrastructure
- [Validation](reference/validation.md) - Validation system
- [Official API Docs](reference/official-api.md) - Official Doxygen documentation (8,704 classes)
- [NET API](reference/net-api.md) - **Workbench TCP/IP API for AI tooling** (ValidateScripts!)

## Other

- [Strategy](strategy.md) - AI tooling decision guide
- [Legal](legal.md) - Legal analysis
- [Session Log](session-log.md) - Research session history
