# Compiler Infrastructure

Components of the Enforce Script compiler discovered in Workbench.

## Core Components

| Component | Namespace | Purpose |
|-----------|-----------|---------|
| `CCompiler` | `enf` | Main compiler class |
| `CompileContext` | - | Compilation context |
| `ParseContext` | - | Parsing context |
| `CParser` | `enf` | Parser |
| `CScriptParser` | `enf` | Script-specific parser |
| `Tokenizer` | `enf` | Lexer/tokenizer |
| `ScriptCompilerContext` | - | Script compilation context |

## Compilation Pipeline

```
Source Code (.c files)
    ↓
Tokenizer@enf (lexical analysis)
    ↓
CParser/CScriptParser@enf (syntax analysis)
    ↓
AST@enf (Abstract Syntax Tree - 24 node types)
    ↓
CCompiler@enf (semantic analysis + IR generation)
    ↓
LLVM 7.0.1 ORC JIT (llvm_7_0_1.dll)
    ↓
Native x64 Machine Code
```

## LLVM JIT Backend

Enforce Script uses **LLVM 7.0.1** for Just-In-Time compilation to native code.

### Key Components

| Component | Purpose |
|-----------|---------|
| `llvm_7_0_1.dll` | LLVM 7.0.1 JIT compiler (9.3 MB) |
| ORC Framework | On-Request Compilation |
| `OrcMCJITReplacement` | JIT execution engine |
| `LinkingORCResolver` | Symbol resolution |

### Evidence

From DLL string analysis:
- Uses LLVM's ORC (On-Request Compilation) infrastructure
- Standard LLVM debug info types (DIBasicType, DICompileUnit, etc.)
- No Enforce-specific modifications to LLVM - pure library

### Implications

1. **Performance**: Scripts compile to native x64 code, not interpreted
2. **Optimization**: LLVM provides industry-standard optimizations
3. **Type Safety**: Type checking happens before LLVM IR generation
4. **No Bytecode**: No intermediate bytecode format (unlike Java/C#)

## Parser Methods

| Method | Purpose |
|--------|---------|
| `ParseFunctionCallSt` | Parse function call statements |
| `ParseArrayCustomClassSt` | Parse array with custom class type |
| `ParseStatementsBodySt` | Parse statement body/block |

## Script Registration

| Component | Purpose |
|-----------|---------|
| `ScriptRegistrator` | Registers script classes |
| `GenerateScriptDeclaration` | Generates declarations |
| `RegisterScriptClasses` | Bulk class registration |
| `ClassRegistrator` | Individual class registration |

## Error Handling

| Component | Purpose |
|-----------|---------|
| `CParseErrorHandler` | Handles parse errors |
| `FirstErrorHandler` | Captures first error |
| `ScriptError` | Script error class |

## Module System

| Component | Purpose |
|-----------|---------|
| `ScriptModule` | Script module class |
| `ScriptModuleRef` | Module reference |

Related errors:
- `Can't compile "%s" script module!`
- `Compilation failed for @"%s"`

## Type System

| Component | Purpose |
|-----------|---------|
| `VarType` | Variable type representation |
| `Variable` | Variable class |
| `Funct` | Function representation |
| `BaseClass` | Base class type |

## Compilation Messages

### Progress Messages

| Message | Meaning |
|---------|---------|
| `Compiling Game scripts` | Game script compilation started |
| `Compiling GameLib scripts` | GameLib compilation started |

### Error Messages

| Message | Meaning |
|---------|---------|
| `Compile error` | Generic compilation error |
| `Compile error: Failing item: %s` | Error with specific item |
| `Can't compile "%s"!` | Module compilation failed |
| `Addon cannot be packed due to failed script compilation!` | Pack blocked by errors |

## Command Line Options

| Option | Description |
|--------|-------------|
| `-loglevel verbose` | Set log verbosity |
| `-nobackend` | Disable backend connection |
| `-nothrow` | Disable exception throwing |
| `-noCrashDialog` | Disable crash dialog |
| `-scriptAuthorizeAll` | Authorize all scripts |
| `-clearsettings` | Clear all settings |
| `-forcesettings` | Force settings |
| `-exitAfterInit` | Exit after initialization |
