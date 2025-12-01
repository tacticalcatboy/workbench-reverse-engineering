# Preprocessor Directives

Enforce Script includes a limited preprocessor for conditional compilation. This reference documents the confirmed and inferred preprocessor capabilities.

## Overview

The Enforce Script preprocessor is **simpler than C/C++** - it primarily supports conditional compilation but lacks many features common to traditional preprocessors.

**Key Limitations:**
- No `#include` for file inclusion
- No `#define` for macros (likely symbols only)
- No function-like macros
- No `defined()` operator found

## Confirmed Directives

### `#ifdef` - If Defined

Compiles the following block only if the symbol is defined.

```c
#ifdef SYMBOL_NAME
    // Code compiled when SYMBOL_NAME is defined
#endif
```

**Evidence:** `CParser: #if[n]def expected an identifier`

### `#ifndef` - If Not Defined

Compiles the following block only if the symbol is NOT defined.

```c
#ifndef SYMBOL_NAME
    // Code compiled when SYMBOL_NAME is NOT defined
#endif
```

**Evidence:** `CParser: #if[n]def expected an identifier`

### `#if` - Conditional Expression

Compiles the following block based on an expression evaluation.

```c
#if EXPRESSION
    // Code compiled when EXPRESSION evaluates to true (non-zero)
#endif
```

**Evidence:** Inferred from the `#if[n]def` error pattern - the `[n]` suggests it handles both `#if` and `#ifndef/ifdef` variants.

## Inferred Directives

These directives are logically necessary but have no direct evidence in the extracted strings:

### `#else`

Provides an alternative branch for conditional compilation.

```c
#ifdef DEBUG
    // Debug code
#else
    // Release code
#endif
```

### `#endif`

Terminates a conditional compilation block.

```c
#ifdef SYMBOL
    // Conditional code
#endif    // Required terminator
```

## Not Supported / No Evidence

The following C/C++ preprocessor features have **no evidence** of support:

| Feature | Status | Notes |
|---------|--------|-------|
| `#include` | Not found | File inclusion appears to be handled at module level |
| `#define VALUE` | Not found | Value macros likely not supported |
| `#define FUNC(x)` | Not found | Function-like macros not supported |
| `#undef` | Not found | Symbol un-definition |
| `#elif` | Not found | Else-if alternative |
| `defined()` | Not found | Operator to test if symbol is defined |
| `#pragma` | Not found | Compiler hints |
| `#error` | Not found | Compilation error directive |
| `#warning` | Not found | Compilation warning directive |
| `#line` | Not found | Line number control |
| `#region` / `#endregion` | Not found | Code folding |
| Token pasting (`##`) | Not found | Macro concatenation |
| Stringification (`#`) | Not found | Macro string conversion |

## Predefined Symbols

### Likely Predefined Symbols

Based on build configurations and extracted strings, these symbols are likely available:

| Symbol | Purpose | Evidence |
|--------|---------|----------|
| `ENABLE_DIAG` | Enable diagnostic features | Found in string extraction |
| `WORKBENCH` | Code running in Workbench | Logical (separate module exists) |
| `DIAG` | Diagnostic build | `%s-DIAG: Error detected` pattern |

### Platform Symbols (Uncertain)

These platform identifiers exist in the binary but may not be preprocessor symbols:

| Symbol | Platform |
|--------|----------|
| `PLATFORM_PC` | PC platform |
| `PLATFORM_WINDOWS` | Windows |
| `PLATFORM_PSN` | PlayStation Network |
| `PLATFORM_XBL` | Xbox Live |

**Note:** These may be enum values or runtime constants rather than preprocessor symbols.

## Syntax Highlighting

The script editor recognizes preprocessor directives:

```
colorPreprocessor  // Editor color setting for preprocessor syntax
```

This confirms preprocessor directives are a recognized language feature with dedicated syntax highlighting.

## Error Messages

| Message | Meaning |
|---------|---------|
| `CParser: #if[n]def expected an identifier` | Symbol name missing after `#ifdef` or `#ifndef` |

## Usage Patterns

### Basic Conditional Compilation

```c
#ifdef DEBUG
    Print("Debug mode enabled");
#endif
```

### Workbench-Only Code

```c
#ifdef WORKBENCH
    // Code that only runs in Workbench editor
#endif
```

### Platform-Specific Code (If Supported)

```c
#ifdef PLATFORM_PC
    // PC-specific implementation
#endif
```

### Diagnostic Code

```c
#ifdef ENABLE_DIAG
    // Diagnostic/profiling code
#endif
```

## Comparison with C Preprocessor

| Feature | C/C++ | Enforce Script |
|---------|-------|----------------|
| `#ifdef` / `#ifndef` | Yes | **Yes** |
| `#if` | Yes | **Likely** |
| `#else` | Yes | **Likely** |
| `#endif` | Yes | **Likely** |
| `#elif` | Yes | Unknown |
| `#include` | Yes | **No** |
| `#define` (simple) | Yes | Unknown |
| `#define` (function) | Yes | **No** |
| `#undef` | Yes | Unknown |
| `#pragma` | Yes | **No** |
| `defined()` | Yes | **No** |

## Best Practices

1. **Use for build variants only** - Conditional compilation should separate debug/release or platform code, not feature toggles
2. **Keep blocks short** - Large conditional blocks make code harder to read
3. **Document symbol meaning** - Comment what each symbol controls
4. **Avoid nesting** - Nested conditionals are hard to follow (nesting support is unverified)

## File Organization Note

Unlike C/C++, Enforce Script does **not** use `#include` for file organization. Instead:

- Scripts are organized into **modules** (Engine, Entities, GameLib, Game, etc.)
- Module dependencies are managed at the project level
- Classes are automatically visible within their module scope
- Cross-module references are handled by the module system

See [Script Modules](../findings/modules.md) for details on the module system.

## Summary

Enforce Script's preprocessor is minimal:
- **Confirmed:** `#ifdef`, `#ifndef`, likely `#if`, `#else`, `#endif`
- **Not Supported:** `#include`, function macros, `#pragma`, `defined()`
- **Unknown:** `#define` (may support simple symbol definition), `#elif`, `#undef`

The preprocessor is primarily useful for conditional compilation based on build configuration, not for code generation or file inclusion.
