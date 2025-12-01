# DLL Analysis - Extract Additional APIs

I'm continuing a Workbench reverse-engineering project to discover additional API methods from Arma Reforger's DLL files.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/index.md - Project overview
2. docs/findings/api.md - Current API surface (1,833 classes, 200+ RPC methods)
3. docs/getting-started/checklist.md - What's been completed

## Context

We've extracted significant API information from the EXE files:
- ArmaReforgerWorkbenchSteamDiag.exe (84,718 strings)
- ArmaReforgerSteamDiag.exe (61,575 strings)

DLLs often contain additional exported functions, type information, and API surfaces not present in the main executables.

## Target DLL Locations

Check these locations for DLLs:
1. Workbench installation directory (same folder as the EXE)
2. `tools/` subdirectory
3. Any `bin/` or `plugins/` directories

Common DLL candidates:
- Engine DLLs (rendering, physics, audio)
- Script runtime DLLs
- Platform-specific DLLs
- Plugin DLLs

## Analysis Tasks

### Task 1: Enumerate DLLs
- List all DLL files in the Workbench/Game directories
- Note file sizes (larger = more likely to have interesting content)
- Group by apparent purpose (engine, script, platform, etc.)

### Task 2: String Extraction
For each significant DLL:
```bash
# Using strings tool or Python script
python scripts/extract_strings.py <dll_path> > data/dlls/<dll_name>_strings.txt
```

### Task 3: Export Table Analysis
Using Ghidra or similar:
- Import each DLL
- Extract exported function names
- Look for patterns:
  - `Script_*` - Script bindings
  - `Enf_*` or `ENF_*` - Enforce engine functions
  - `Register*` - Registration functions
  - `Create*`, `Get*`, `Set*` - Factory/accessor patterns
  - Namespace prefixes matching known namespaces (enf, gamelib, etc.)

### Task 4: Cross-Reference with EXE Findings
Compare DLL exports against:
- Known ClassRegistrator classes
- Method signatures found in EXE strings
- Missing methods referenced in error messages

## Search Patterns

Look for these patterns in DLL strings/exports:

**Class/Method Registration:**
- `ClassRegistrator`
- `MethodRegistrator`
- `PropertyRegistrator`
- `RegisterScriptClass`
- `RegisterMethod`

**API Namespaces:**
- `enf::` - Engine core
- `gamelib::` - Game library
- `gamecode::` - Game code
- `ailib::` - AI systems
- `ast::` - AST/compiler

**Method Categories:**
- Native bindings: `native`, `extern`, `__declspec`
- Callbacks: `Callback`, `Delegate`, `Invoker`
- Events: `Event`, `Handler`, `Listener`
- Serialization: `Serialize`, `Deserialize`, `Read`, `Write`

## Output

### Create new data files:
- `data/dlls/` - Directory for DLL string extracts
- `data/dlls/dll_inventory.txt` - List of DLLs with sizes/purposes

### Update documentation:
- `docs/findings/api.md` - Add new methods/classes discovered
- `docs/findings/modules.md` - If module structure is clarified

### Update checklist:
When complete, move "Explore DLL files for additional APIs" to Completed in `docs/getting-started/checklist.md`

## Expected Discoveries

DLLs may reveal:
1. Native method bindings not visible in EXE strings
2. Internal engine APIs
3. Plugin/extension interfaces
4. Platform-specific implementations
5. Debug/diagnostic functions
6. Serialization format details

## Notes

- Focus on DLLs that appear script-related first
- Large DLLs with many exports are higher priority
- Compare findings across Workbench vs Game directories (some DLLs may differ)
- Watch for version strings that confirm DLL purposes
