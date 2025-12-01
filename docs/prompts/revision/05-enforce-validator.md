# 05 - Build Enforce Script Validator

Replicate the Workbench Enforce Script validator for standalone use.

## Context

We've reverse-engineered the Arma Reforger Workbench to understand Enforce Script:
- **84,718 strings** extracted from Workbench EXE
- **8,704 API classes** documented (Enfusion + Arma Reforger)
- **270+ diagnostic patterns** discovered
- **40+ keywords** identified
- **24 AST node types** mapped
- **LLVM 7.0.1** used for JIT (backend only, not relevant to validation)

## Goal

Build a standalone Enforce Script validator that can:
1. Parse `.c` source files
2. Build an AST
3. Perform semantic analysis
4. Report errors, warnings, and hints matching Workbench output

## Strategy

| Component | Purpose |
|-----------|---------|
| **This Validator** | Primary development tool, fast feedback |
| **Workbench** | Final checks, Workshop upload, in-game debugging |
| **NET API** | Optional - test `ValidateScripts` TCP API as supplement |

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Enforce Script Validator            │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Source Code (.c files)                              │
│         │                                            │
│         ▼                                            │
│  ┌─────────────┐                                     │
│  │   Lexer     │  ← keywords.md, grammar.md          │
│  │ (Tokenizer) │                                     │
│  └──────┬──────┘                                     │
│         │ Tokens                                     │
│         ▼                                            │
│  ┌─────────────┐                                     │
│  │   Parser    │  ← grammar.md, ast-nodes.md         │
│  │             │                                     │
│  └──────┬──────┘                                     │
│         │ AST                                        │
│         ▼                                            │
│  ┌─────────────┐                                     │
│  │  Semantic   │  ← api.md, types.md, attributes.md  │
│  │  Analyzer   │                                     │
│  └──────┬──────┘                                     │
│         │                                            │
│         ▼                                            │
│  ┌─────────────┐                                     │
│  │ Diagnostics │  ← diagnostics.md, runtime-errors.md│
│  │  Reporter   │                                     │
│  └─────────────┘                                     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## Resources Available

### Grammar & Syntax
| Resource | Location | Contents |
|----------|----------|----------|
| Grammar | `docs/reference/grammar.md` | Operators, precedence, statements |
| Keywords | `docs/findings/keywords.md` | 40+ keywords with evidence |
| AST Nodes | `docs/reference/ast-nodes.md` | 24 node types |
| Attributes | `docs/reference/attributes.md` | 20+ attributes |
| Preprocessor | `docs/reference/preprocessor.md` | #ifdef/#ifndef support |

### Type System
| Resource | Location | Contents |
|----------|----------|----------|
| Types | `docs/findings/types.md` | Built-in types (int, float, vector, etc.) |
| API Surface | `docs/findings/api.md` | 1,833 ClassRegistrator entries |
| Class Hierarchy | `docs/findings/class-hierarchy.md` | Inheritance patterns |
| Official API | Doxygen HTML | 8,704 classes with full signatures |

### Validation Rules
| Resource | Location | Contents |
|----------|----------|----------|
| Diagnostics | `docs/findings/diagnostics.md` | 120+ compile-time patterns |
| Runtime Errors | `docs/findings/runtime-errors.md` | 150+ runtime patterns |
| Compiler | `docs/reference/compiler.md` | Compilation pipeline |
| Validation | `docs/reference/validation.md` | Validation system |

### Raw Data
| Resource | Location | Contents |
|----------|----------|----------|
| Workbench Strings | `data/workbench/all_strings.txt` | 84,718 strings |
| Game Strings | `data/game/all_strings.txt` | 61,575 strings |
| LLVM Strings | `data/dlls/llvm_strings.txt` | 35,118 strings |
| DLL Inventory | `data/dlls/dll_inventory.md` | DLL analysis summary |

## Implementation Steps

### Phase 1: Lexer
**Input:** Source code string
**Output:** Token stream

1. Implement token types:
   ```
   KEYWORD, IDENTIFIER, NUMBER, STRING, VECTOR_LITERAL,
   OPERATOR, PUNCTUATION, ATTRIBUTE_START, COMMENT, NEWLINE, EOF
   ```

2. Implement keyword recognition (from `keywords.md`):
   ```
   class, extends, modded, sealed, abstract, override,
   ref, autoptr, weak, notnull, owned,
   static, const, private, protected,
   if, else, for, foreach, while, do, switch, case, default,
   return, break, continue, null, true, false, this, super,
   new, delete, thread, typename, typedef, enum, void,
   native, volatile, out, inout, proto
   ```

3. Handle special literals:
   - Vector: `"1.0 2.0 3.0"` (string with 3 floats = vector)
   - ResourceName: `"{GUID}path/to/resource"`

### Phase 2: Parser
**Input:** Token stream
**Output:** Abstract Syntax Tree

1. Implement AST node types (from `ast-nodes.md`):
   ```
   // Declarations
   CScriptFile, CClassDecl, CFunctionDecl, CVarDecl, CEnumDecl

   // Statements
   CBlockSt, CIfSt, CForSt, CForEachSt, CWhileSt, CDoWhileSt,
   CSwitchSt, CCaseSt, CReturnSt, CBreakSt, CContinueSt,
   CExpressionSt, CVarDeclSt

   // Expressions
   CBinaryExpr, CUnaryExpr, CCallExpr, CMemberExpr, CIndexExpr,
   CIdentExpr, CLiteralExpr, CCastExpr, CNewExpr, CTernaryExpr
   ```

2. Parse class declarations:
   ```
   [Attribute(params)]
   modded class ClassName extends BaseClass : Interface
   {
       // members
   }
   ```

3. Parse function declarations:
   ```
   [Attribute]
   proto native void FunctionName(out int param, string name = "default");
   override protected static int AnotherFunc() { ... }
   ```

### Phase 3: Semantic Analyzer
**Input:** AST
**Output:** Validated AST + Diagnostics

1. **Symbol Table**
   - Build scope hierarchy (file → class → function → block)
   - Register all declarations
   - Resolve references

2. **Type Checking**
   - Verify assignment compatibility
   - Check function call arguments
   - Validate operator usage

3. **API Validation**
   - Load 8,704 class definitions from parsed API docs
   - Validate method calls against known signatures
   - Check inheritance requirements

4. **Attribute Validation**
   - Verify attribute parameters
   - Check attribute applicability (class vs method vs property)

### Phase 4: Diagnostic Reporter
**Input:** Validation errors
**Output:** Formatted diagnostics

Match Workbench error format:
```
SCRIPT  (E): path/to/file.c(42): error message here
SCRIPT  (W): path/to/file.c(15): warning message here
SCRIPT  (H): path/to/file.c(8): hint message here
```

## Validation Checklist

Test against known Workbench behavior:

- [ ] Parse official game scripts without syntax errors
- [ ] Detect undefined variable usage
- [ ] Detect type mismatches
- [ ] Detect missing method overrides
- [ ] Detect incorrect attribute usage
- [ ] Detect deprecated API usage
- [ ] Match Workbench error messages for known test cases

## Technology Options

| Option | Pros | Cons |
|--------|------|------|
| **Python + Lark** | Fast to develop, readable | Slower runtime |
| **TypeScript** | Good tooling, fast enough | More verbose |
| **Rust + tree-sitter** | Very fast, reusable grammar | Steeper learning curve |
| **C# + ANTLR** | .NET ecosystem, mature | Heavier dependencies |

Recommendation: Start with **Python + Lark** for rapid prototyping, optimize later if needed.

## Output Locations

```
tools/
├── enforce-validator/
│   ├── src/
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   ├── ast.py
│   │   ├── analyzer.py
│   │   ├── diagnostics.py
│   │   └── api_loader.py
│   ├── grammar/
│   │   └── enforce.lark
│   ├── tests/
│   │   ├── test_lexer.py
│   │   ├── test_parser.py
│   │   └── test_analyzer.py
│   ├── requirements.txt
│   └── README.md
```

## Success Criteria

1. **Parses valid code** - No false syntax errors on official game scripts
2. **Catches real errors** - Detects errors that Workbench would catch
3. **Helpful messages** - Error messages include file, line, and clear description
4. **Fast enough** - Validates a typical mod (<100 files) in under 5 seconds
5. **Matches Workbench** - Same errors on same input (verified via final checks)

## Next Steps After Completion

1. Integrate with IDE extensions (VS Code)
2. Add auto-fix suggestions for common errors
3. Test NET API as alternative/supplement
4. Create CI/CD pipeline for mod projects
