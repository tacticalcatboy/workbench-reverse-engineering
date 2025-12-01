# DLL Inventory - Arma Reforger Workbench & Game

Analysis of DLL files for API discovery.

## Summary

**Key Finding:** No Enforce Script-specific DLLs exist. All script compilation, parsing, and API binding is embedded in the main executables. The DLLs are standard third-party libraries.

## Workbench DLLs

Location: `D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\`

| DLL | Size | Purpose | Relevance |
|-----|------|---------|-----------|
| **llvm_7_0_1.dll** | 9.3 MB | LLVM 7.0.1 compiler infrastructure | **HIGH** - JIT compilation backend |
| Qt6Gui.dll | 8.9 MB | Qt Framework - GUI rendering | Low - UI only |
| Qt6Widgets.dll | 6.2 MB | Qt Framework - Widget library | Low - UI only |
| Qt6Core.dll | 5.9 MB | Qt Framework - Core utilities | Low - UI only |
| Qt6Network.dll | 1.7 MB | Qt Framework - Network operations | Low - UI only |
| Compressonator_MD_DLL.dll | 1.6 MB | AMD texture compression | Low - Asset pipeline |
| OpenXLSX.dll | 311 KB | Excel file reading/writing | Low - Data import |
| steam_api64.dll | 292 KB | Steam integration | None |
| amd_ags_x64.dll | 172 KB | AMD GPU Services | None |
| platforms/qwindows.dll | - | Qt Windows platform plugin | None |

## Game DLLs

Location: `D:\SteamLibrary\steamapps\common\Arma Reforger\`

| DLL | Size | Purpose | Relevance |
|-----|------|---------|-----------|
| steam_api64.dll | 292 KB | Steam integration | None |
| amd_ags_x64.dll | 172 KB | AMD GPU Services | None |
| battleye/BEClient_x64.dll | - | BattlEye anti-cheat client | None |
| battleye/BEServer_x64.dll | - | BattlEye anti-cheat server | None |

## LLVM 7.0.1 Analysis

### Strings Extracted
- **Total strings:** 35,118
- **Saved to:** `data/dlls/llvm_strings.txt`

### Key Findings

1. **ORC JIT Infrastructure**
   - Uses LLVM's On-Request Compilation (ORC) framework
   - `OrcMCJITReplacement` - replacement for older MCJIT
   - `LinkingORCResolver` - symbol resolution
   - `MCJITReplacementMemMgr` - memory management

2. **Standard LLVM Types**
   - DIBasicType, DICompileUnit, DICompositeType
   - DIDerivedType, DISubroutineType
   - Standard debug info metadata

3. **No Enforce-Specific Modifications**
   - Pure LLVM 7.0.1 library
   - All script-specific code is in the main EXE

### Compilation Flow (Inferred)

```
Enforce Script Source (.c files)
        |
        v
   [CParser@enf] - Parsing (in EXE)
        |
        v
   [AST@enf] - Abstract Syntax Tree (in EXE)
        |
        v
   [CCompiler@enf] - Compilation (in EXE)
        |
        v
   [LLVM IR Generation] - (in EXE, calls LLVM DLL)
        |
        v
   [llvm_7_0_1.dll] - JIT to native x64
        |
        v
   Native Machine Code
```

## Conclusions

1. **DLLs do not contain additional API surface**
   - All 8,704 documented classes are exposed through the main EXE
   - The DLLs are purely support libraries

2. **Script compilation uses LLVM JIT**
   - Enforce Script is compiled to native code at runtime
   - Uses LLVM 7.0.1's ORC framework for on-demand compilation
   - This explains the high performance of scripts

3. **No plugin system discovered**
   - No evidence of DLL-based plugin architecture
   - All functionality is statically linked in the EXE

4. **UI is Qt-based**
   - Workbench uses Qt 6 for its interface
   - Standard Qt Framework, no custom modifications visible

## Recommendations

For further API discovery:
1. Focus analysis on the main Workbench EXE (64 MB)
2. The official API documentation (8,704 classes) is comprehensive
3. Internal/native APIs would require deeper EXE reverse engineering
