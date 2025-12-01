# Grammar & Syntax Analysis

I'm continuing a Workbench reverse-engineering project to document Enforce Script grammar and syntax rules.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/findings/keywords.md - 35+ confirmed keywords, 24 AST node types
2. docs/reference/ast-nodes.md - AST structure
3. docs/reference/compiler.md - Compiler infrastructure

## Context

We've discovered significant language structure from error messages:
- 35+ confirmed keywords with evidence
- 24 AST node types (ForLoopNode, ClassDefNode, etc.)
- Parser error patterns revealing syntax expectations

## Analysis Tasks

### Task 1: Parser Error Mining
Search for parser-related error messages that reveal syntax rules:

```
Patterns to search:
- "expected" - What tokens are expected where
- "unexpected" - Invalid syntax patterns
- "character %d" - Position-based errors
- "CParser:" - Direct parser messages
- "Syntax" - Syntax errors
- "Expression" - Expression rules
- "Statement" - Statement rules
```

### Task 2: Operator Precedence
Look for evidence of operator precedence:
- Binary operators: `+`, `-`, `*`, `/`, `%`, `&`, `|`, `^`, `<<`, `>>`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `&&`, `||`, `!`
- Assignment: `=`, `+=`, `-=`, etc.
- Ternary: `?:`

### Task 3: Statement Syntax
Document syntax for each statement type:

| Statement | Syntax Pattern | Evidence |
|-----------|---------------|----------|
| if | `if (expr) stmt [else stmt]` | BranchNode |
| for | `for (init; cond; iter) stmt` | ForLoopNode |
| foreach | `foreach (var : collection) stmt` | ForeachLoopNode |
| while | `while (expr) stmt` | WhileLoopNode |
| switch | `switch (expr) { cases }` | SwitchNode |
| return | `return [expr];` | Error messages |

### Task 4: Declaration Syntax
Document declaration patterns:

**Variables:**
```
[modifiers] type name [= initializer];
modifiers: static, const, auto, ref, autoptr, weak, notnull
```

**Functions:**
```
[modifiers] returnType name([params]) [override] { body }
modifiers: static, native, override, sealed, private, protected
```

**Classes:**
```
[modded] [sealed] class Name [: BaseClass] { members }
```

**Enums:**
```
enum Name { VALUE1, VALUE2 = expr, ... }
```

### Task 5: Expression Syntax
Document expression forms:
- Literals: numbers, strings, booleans, null
- Identifiers and qualified names
- Array access: `arr[index]`
- Member access: `obj.member`
- Method calls: `obj.method(args)`
- New expressions: `new ClassName(args)`
- Cast expressions: `(Type)expr` or function-style
- Ternary: `cond ? true_expr : false_expr`

### Task 6: Attribute Syntax
Confirm attribute placement and parameters:
```
[AttributeName]
[AttributeName(param)]
[AttributeName(name = value)]
```

## Search Patterns

```bash
# Parser errors
grep -i "expected" data/workbench/all_strings.txt
grep -i "CParser" data/workbench/all_strings.txt

# Syntax hints
grep -i "syntax" data/workbench/all_strings.txt
grep -i "expression" data/workbench/all_strings.txt
grep -i "statement" data/workbench/all_strings.txt

# Operators
grep -E "\|\||&&|==|!=" data/workbench/all_strings.txt
```

## Output

### Update/Create:
- `docs/reference/grammar.md` - Full grammar documentation
- `docs/findings/keywords.md` - Add any new keywords discovered

### Document:
- Statement syntax with examples
- Expression syntax with examples
- Declaration syntax with examples
- Operator precedence table
- Reserved words list

## Goal

Create a grammar reference sufficient for:
1. AI to generate syntactically correct code
2. Understanding what syntax patterns are valid/invalid
3. Predicting what errors will occur for invalid syntax

## When Complete

Update `docs/getting-started/checklist.md`:
- Move "Study grammar/syntax behavior in depth" to Completed
