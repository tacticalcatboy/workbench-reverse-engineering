# Progress Checklist

Track what's been completed and what remains.

## Completed

- [x] Install JDK 21 and Ghidra 11.4.2
- [x] Import `ArmaReforgerWorkbenchSteamDiag.exe` into Ghidra
- [x] Extract 84,718 strings from Workbench binary
- [x] Extract 61,575 strings from Game binary
- [x] Identify 120+ diagnostic patterns
- [x] Discover AST node types (19)
- [x] Map compiler infrastructure
- [x] Find validation system components
- [x] Document log levels (7 levels)
- [x] Compare Workbench vs Game strings
- [x] Identify 150+ runtime-only diagnostics
- [x] Deep search game strings for missed patterns
- [x] Extract more API method signatures (373 RPC methods, 30 EOn* events, 30+ widget handlers, 40+ AI tasks)
- [x] Research script module system (6 modules: Engine, Entities, GameLib, Game, Workbench, WorkbenchGame)
- [x] Complete keyword list (40+ confirmed keywords with evidence, 24 AST node types)
- [x] Discover official API docs (8,704 classes with full method signatures!)
- [x] Document Workbench NET API (limited external use - internal files only)
- [x] Verify reverse-engineered findings against official docs (all confirmed accurate!)
- [x] Study grammar/syntax behavior in depth (comprehensive grammar.md created)
- [x] Document attribute parameter rules (comprehensive attributes.md created with 20+ attributes)
- [x] Map full preprocessor directive support (limited preprocessor - #ifdef/#ifndef confirmed, no #include/#define)
- [x] Map class relationships (inheritance, composition, dependencies) - see class-hierarchy.md

## In Progress

None at this time

## Planned

- [ ] Parse official API docs into structured format (JSON/markdown)

## Completed (DLL Analysis)

- [x] Explore DLL files for additional APIs
  - Analyzed 10 Workbench DLLs and 4 Game DLLs
  - **Key finding:** LLVM 7.0.1 used for JIT compilation
  - No Enforce Script-specific DLLs - all APIs in main EXE
  - See: `data/dlls/dll_inventory.md`

## Research Questions

### Answered

- ~~Internal severity system~~ - 7 LogLevels (Fatal to Spam)
- ~~Error codes~~ - No numeric codes, uses string messages
- ~~AST structure~~ - 19 node types discovered
- ~~Validation system~~ - EScriptValidationResult, EntityValidationBase, etc.
- ~~Script module system~~ - 6 modules (Engine, Entities, GameLib, Game, Workbench, WorkbenchGame), hierarchical dependencies, cross-module type checking

### Open Questions

1. How does Workbench determine "unused" variables?
2. What triggers the "can be const" hint?
3. Full attribute parameter validation rules?

## Statistics

| Category | Workbench | Game | Shared |
|----------|-----------|------|--------|
| Total Strings | 84,718 | 61,575 | 52,890 |
| Unique Strings | 31,828 | 1,067 | - |
| Diagnostics | 120+ | 150+ (runtime) | Many |
| RPC Methods | 373 | - | - |
| EOn* Event Handlers | 30 | - | - |
| Widget Event Handlers | 30+ | - | - |
| AI Task Classes | 40+ | - | - |
| Component Classes | 100+ | - | - |
| Script Modules | 6 (incl. WB) | 4 | 4 |

### Official API Documentation

| API | Classes | Description |
|-----|---------|-------------|
| EnfusionScriptAPIPublic | 824 | Engine API |
| ArmaReforgerScriptAPIPublic | 7,880 | Game API |
| **Total** | **8,704** | Full method signatures |
