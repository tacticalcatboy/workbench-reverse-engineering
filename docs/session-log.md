# Session Log

History of research sessions.

## Session 7: 2025-11-27

### Major Discoveries

**Official API Documentation Found!**

- Location: `D:\SteamLibrary\...\Workbench\docs\`
- EnfusionScriptAPIPublic: 824 classes
- ArmaReforgerScriptAPIPublic: 7,880 classes
- **Total: 8,704 classes with full method signatures!**

**NET API Status Clarified**

- ValidateScripts exists but limited to internal Workbench files
- Community (bacon) couldn't get external validation working
- Not viable for external AI tooling currently

**BI Official Tooling Coming!**

- Arkensor (BI staff) confirmed plans for EnforceScript CLI tools
- Linter, syntax/compile checker in early prototyping
- Timeline uncertain - recommends waiting a few months
- Strategy shift: Focus on AI-specific tooling that complements official tools

### Verification

- All reverse-engineered findings verified against official docs
- EOn* event signatures confirmed accurate
- RPC method patterns confirmed

### Documentation Updates

- Created `reference/official-api.md`
- Created `reference/net-api.md`
- Updated `strategy.md` with new recommended approach
- Updated `checklist.md` with discoveries
- Updated `mkdocs.yml` navigation

### Strategic Shift

- **Before:** Reverse-engineer everything from binary
- **After:** Use official docs + NET API for AI tooling
- NET API ValidateScripts = authoritative validation without reverse-engineering parser

---

## Session 6: 2025-11-26

### Project Restructure

- Reorganized project structure for MkDocs documentation site
- Created folder hierarchy: `docs/`, `data/`, `scripts/`, `tools/`
- Set up MkDocs with Material theme (GitHub-style)
- Split documentation into focused pages

### New Structure

```
workbench-reverse-engineering/
├── docs/           # Documentation site
│   ├── index.md
│   ├── getting-started/
│   ├── findings/
│   └── reference/
├── data/           # Extracted strings
│   ├── workbench/
│   └── game/
├── scripts/        # Python/Java scripts
└── tools/          # Ghidra installation
```

---

## Session 5: 2025-11-24

### Game Executable Analysis

- Imported `ArmaReforgerSteamDiag.exe` into Ghidra
- Extracted 61,575 strings from game
- Comparison with Workbench:
  - Game only: 1,067 strings (runtime-specific)
  - Workbench only: 31,828 strings (editor/compile-time)
  - Shared: 52,890 strings (core engine)
- Found 67 runtime-specific diagnostics

### AST Deep Dive

- Discovered complete AST hierarchy (19 node types)
- Found parser methods (ParseFunctionCallSt, etc.)
- Mapped validation system components
- Found type system components (VarType, Variable, Funct)

### New Error Categories

- Syntax errors (brackets, EOF)
- Undefined/Unknown errors
- Return type errors
- Static context errors
- RPC/Replication errors
- Enum errors
- Array/Index errors

---

## Session 4: 2025-11-24

### Deep Unknown Research

- **Log Levels CONFIRMED:** 7 levels (Fatal → Spam)
- Command line options discovered
- Diagnostic menu system found
- Config files identified
- Warning suppression researched (no pragma/nowarn found)
- ScriptCompilerContext discovered

---

## Session 3: 2025-11-24

### Infrastructure Research

- Researched severity system → Found LogLevelRegistrator
- Found 1,833 ClassRegistrator entries
- Discovered compiler components (CCompiler, ParseContext, Tokenizer)
- Confirmed no numeric error codes
- Identified trigger condition patterns

---

## Session 2: 2025-11-24

### Deep Diagnostic Extraction

- Deep searched all 96,939 strings
- Found 80+ verified diagnostic patterns (up from 10)
- Categorized into 11 major categories
- Key discoveries:
  - Inheritance/override errors
  - Constructor/serialization requirements
  - Callback validation
  - Attribute validation
  - Template compilation errors

---

## Session 1: 2025-11-24

### Initial Setup

- Set up Ghidra project
- Extracted strings from Workbench executable
- Identified initial 10 diagnostic patterns
- Created strategy document
- Decision: Start fresh, discard prior assumptions

---

## Statistics Over Time

| Session | Diagnostics Found | Strings Analyzed | Notes |
|---------|------------------|------------------|-------|
| 1 | 10 | 96,939 | Initial setup |
| 2 | 80+ | 96,939 | Deep extraction |
| 3 | 100+ | 96,939 | Infrastructure |
| 4 | 110+ | 96,939 | Log levels |
| 5 | 120+ | 158,293 | Game exe added |
| 6 | 120+ | - | Restructure |
| 7 | 270+ | - | **+8,704 API classes from official docs!** |
