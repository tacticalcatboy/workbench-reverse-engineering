# Preprocessor Directive Support

I'm continuing a Workbench reverse-engineering project to map Enforce Script preprocessor directive support.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/findings/keywords.md - Known preprocessor directives (#if, #ifdef, #ifndef)
2. docs/reference/compiler.md - Compiler infrastructure

## Context

Confirmed preprocessor directives:
- `#if` - Conditional compilation
- `#ifdef` - If defined
- `#ifndef` - If not defined

Likely but unconfirmed:
- `#else` - Else branch
- `#endif` - End conditional
- `#define` - Define macro/constant
- `#include` - Include file (uncertain)

Evidence: `CParser: #if[n]def expected an identifier`

## Analysis Tasks

### Task 1: Directive Error Messages
Search for preprocessor-related errors:

```
Patterns:
- "#" at start of line
- "CParser: #"
- "directive"
- "preprocessor"
- "define"
- "ifdef"
- "ifndef"
- "endif"
- "include"
- "macro"
```

### Task 2: Conditional Compilation
Document conditional compilation:

```
#ifdef SYMBOL
    // code when SYMBOL is defined
#endif

#ifndef SYMBOL
    // code when SYMBOL is not defined
#endif

#if EXPRESSION
    // code when EXPRESSION is true
#else
    // code when EXPRESSION is false
#endif
```

Questions to answer:
- What expressions are valid in `#if`?
- Can `#if` use defined()?
- Is `#elif` supported?
- Can directives be nested?

### Task 3: Symbol Definition
Document how symbols are defined:

```
#define SYMBOL
#define SYMBOL value
#define SYMBOL(args) expansion  // function-like macro?
```

Questions:
- Can #define have values?
- Are function-like macros supported?
- How to undefine (#undef)?
- Predefined symbols (DEBUG, PLATFORM, etc.)?

### Task 4: File Inclusion
Check if file inclusion exists:

```
#include "path/file.c"
#include <system_file>
```

Questions:
- Is #include supported at all?
- Relative vs absolute paths?
- Search path behavior?
- Include guards?

### Task 5: Other Directives
Check for additional directives:

```
#pragma - Compiler hints
#error - Compilation error
#warning - Compilation warning
#line - Line number control
#region / #endregion - Code folding
```

## Search Patterns

```bash
# Direct directive searches
grep "^#" data/workbench/all_strings.txt
grep -i "CParser.*#" data/workbench/all_strings.txt

# Directive keywords
grep -i "ifdef\|ifndef\|endif\|define\|include" data/workbench/all_strings.txt
grep -i "directive\|preprocessor" data/workbench/all_strings.txt
grep -i "macro" data/workbench/all_strings.txt

# Predefined symbols
grep -i "DEBUG\|RELEASE\|PLATFORM" data/workbench/all_strings.txt
grep -i "WORKBENCH\|DIAG\|EDITOR" data/workbench/all_strings.txt
```

## Expected Predefined Symbols

Likely predefined based on build configurations:
- `WORKBENCH` - Defined in Workbench builds
- `DIAG` or `DIAGNOSTICS` - Diagnostic builds
- `DEBUG` / `RELEASE` - Build type
- `PLATFORM_*` - Platform detection
- `SERVER` / `CLIENT` - Network role

## Output

### Create:
- `docs/reference/preprocessor.md` - Complete preprocessor reference

### Document:
- All supported directives with syntax
- Predefined symbols
- Conditional compilation patterns
- Common usage patterns
- Error messages and their meanings

### Update:
- `docs/findings/keywords.md` - Add confirmed directives
- `docs/getting-started/checklist.md` - Mark task complete

## Goal

Create a preprocessor reference sufficient for:
1. AI to use conditional compilation correctly
2. Understanding what preprocessing is available
3. Platform/build-specific code patterns

## When Complete

Update `docs/getting-started/checklist.md`:
- Move "Map full preprocessor directive support" to Completed
