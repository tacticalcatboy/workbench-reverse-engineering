# Keywords & Modifiers

Language keywords discovered through error messages, compiler infrastructure, and AST analysis.

## Access Modifiers

| Keyword | Evidence |
|---------|----------|
| `private` | `'%s.%s': cannot override inherited member '%s' because it is private` |
| `protected` | `Private conflicts with protected`, `Method '%s' is protected` |
| `public` | `Can't clone class '%s', constructor is not public` |

## Class Modifiers

| Keyword | Evidence |
|---------|----------|
| `sealed` | `'%s': cannot derive from sealed type '%s'`, `Sealed type '%s' can't be modded` |
| `abstract` | `abstract systems cannot be created` |
| `modded` | `'vanilla' keyword can be used only in modded classes` |

**Parser Regex Evidence:** `^(\s*\bmodded\b|\s*\bsealed\b)*\s*(\bclass\b|\benum\b)+\s(\w+)`

## Member Modifiers

| Keyword | Evidence |
|---------|----------|
| `override` | `Function '%s' is marked as override, but there is no function with this name in the base class` |
| `static` | `Function '%s' override signature conflict: differing 'static' usage` |
| `native` | `Script function cannot be native '%s'`, `Native functions don't support 'out' arguments '%s'` |

## Reference & Pointer Keywords

| Keyword | Evidence |
|---------|----------|
| `ref` | `Variable '%s' is not strong ref (missing 'ref' keyword?)` |
| `notnull` | `'notnull' must not be used with '%s' type` |
| `autoptr` | `autoptr/ref in template is not supported on non-managed class '%s'` |
| `weak` | `Script variable '%s.%s': using weak pointer to store object, use 'ref' for strong reference` |

## Storage Modifiers

| Keyword | Evidence |
|---------|----------|
| `const` | `Variable '%s' can be const`, `static/const variables can't be auto` |
| `auto` | `static/const variables can't be auto` |

## Parameter Modifiers

| Keyword | Evidence |
|---------|----------|
| `out` | `Native functions don't support 'out' arguments '%s'` |
| `inout` | `inout/out/notnull can be used only on function parameters` |

## Type Definition Keywords

| Keyword | Evidence |
|---------|----------|
| `class` | AST: `ClassDefNode@ast@enf`, Parser regex confirms |
| `enum` | AST: `EnumDefNode@ast@enf`, Parser regex confirms |
| `typedef` | `Circle inheritance in typedef '%s'` |

## Type Keywords

| Keyword | Evidence |
|---------|----------|
| `void` | `Can't compare 'void' type`, `Can't condition 'void' type` |
| `typename` | `Can't get typename from forward declaration '%s'`, `Static array of 'typename' types is not supported` |

## Built-in Primitive Types

| Type | Evidence |
|------|----------|
| `int` | `FileHandle.Read: unsupported type (supported types: int,float,string)` |
| `float` | `FileHandle.Read: unsupported type (supported types: int,float,string)` |
| `string` | `FileHandle.Read: unsupported type (supported types: int,float,string)` |
| `bool` | `'%s' not supported on 'bool'` |

## Built-in Complex Types

| Type | Evidence |
|------|----------|
| `array<T>` | `enf::Array<...>`, `@array<vector>` |
| `vector` | `@array<vector>`, `Vector3`, `Vector4` in C++ types |
| `ResourceName` | `use ResourceName type instead`, `array<ResourceName>` |

## Control Flow Keywords

Evidence from AST node types in `ast@enf` namespace:

| Keyword | AST Node |
|---------|----------|
| `for` | `ForLoopNode@ast@enf` |
| `foreach` | `ForeachLoopNode@ast@enf` |
| `while` | `WhileLoopNode@ast@enf` |
| `switch` | `SwitchNode@ast@enf` |
| `case` | `CaseNode@ast@enf` |
| `if` | `BranchNode@ast@enf` (branching) |
| `return` | `No return statement in function returning non-void '%s'` |

**Additional Control Flow Keywords:**

| Keyword | Evidence |
|---------|----------|
| `else` | Paired with `if` (standard, `BranchNode` handles both) |
| `break` | `Misplaced break/case/continue` |
| `continue` | `Misplaced break/case/continue` |
| `default` | Switch default case (standard with `SwitchNode`/`CaseNode`) |

## Special Keywords

| Keyword | Evidence |
|---------|----------|
| `vanilla` | `'vanilla' keyword can be used only in modded classes` |
| `this` | `'this' or 'super' inside static method is not valid` |
| `super` | `'this' or 'super' inside static method is not valid` |
| `thread` | `Cannot create thread out of non-script function '%s'` |

## Operator Keywords

| Keyword | AST Node / Evidence |
|---------|---------------------|
| `new` | `NewOp@ast@enf` |

## Literals

| Literal | Evidence |
|---------|----------|
| `null` | `Only null assignment is allowed on plain data` |
| `NULL` | `Only NULL assignment is allowed` |
| `true` | Boolean literal (used in docs/messages) |
| `false` | Boolean literal (used in docs/messages) |

## Preprocessor Directives

| Directive | Status | Evidence |
|-----------|--------|----------|
| `#ifdef` | **Confirmed** | `CParser: #if[n]def expected an identifier` |
| `#ifndef` | **Confirmed** | `CParser: #if[n]def expected an identifier` |
| `#if` | **Likely** | Inferred from `#if[n]def` error pattern |
| `#else` | **Likely** | Logically required for conditionals |
| `#endif` | **Likely** | Logically required for conditionals |

### Not Supported / No Evidence

| Directive | Status |
|-----------|--------|
| `#include` | **Not found** - File inclusion handled at module level |
| `#define` (macros) | **Not found** - No macro support |
| `#undef` | **Not found** |
| `#elif` | **Not found** |
| `#pragma` | **Not found** |
| `#error` / `#warning` | **Not found** |
| `#region` / `#endregion` | **Not found** |
| `defined()` operator | **Not found** |

**Note:** The preprocessor is limited to conditional compilation. See [Preprocessor Reference](../reference/preprocessor.md) for details.

## RPC/Replication Keywords

| Keyword | Evidence |
|---------|----------|
| `RPC` | `RPC '%s.%s' has parameters that cannot be replicated` |
| `replicated` | `Variable '%s.%s' is marked as replicated property` |

## Attribute Syntax

Attributes use **square bracket syntax** `[AttributeName]`:

| Attribute | Evidence |
|-----------|----------|
| `[EventAttribute]` | `Method '%s.%s' is not marked with the [EventAttribute] attribute.` |
| `[ReceiverAttribute]` | `Method '%s.%s' is not marked with the [ReceiverAttribute] attribute.` |

## AST Node Types Summary

Complete list of AST nodes discovered in `ast@enf` namespace:

| Node Type | Purpose |
|-----------|---------|
| `BinaryOp` | Binary operators (+, -, *, /, etc.) |
| `BranchNode` | Conditional branching (if/else) |
| `CallOp` | Function/method calls |
| `CaseNode` | Switch case statements |
| `CastNode` | Type casting |
| `ClassDefNode` | Class definitions |
| `CommandNode` | Commands |
| `EnumDefNode` | Enum definitions |
| `ExpressionNode` | General expressions |
| `ForLoopNode` | For loops |
| `ForeachLoopNode` | Foreach loops |
| `FuncDefNode` | Function definitions |
| `LeafNode` | Leaf nodes (literals, identifiers) |
| `ListNode` | List nodes |
| `NewOp` | New operator |
| `Node` | Base node class |
| `StatementNode` | Statements |
| `SwitchNode` | Switch statements |
| `SyntaxTreeNodeBase` | Base syntax tree node |
| `TypeDefNode` | Type definitions (typedef) |
| `TypeNode` | Type references |
| `UnaryOp` | Unary operators (-, !, etc.) |
| `VarNode` | Variable references |
| `WhileLoopNode` | While loops |

## Parser Messages

Parser-related messages that reveal language structure:

| Message | Reveals |
|---------|---------|
| `Expected name, not a keyword '%s'` | Keywords are reserved |
| `Identifier expected (character %d)` | Identifier syntax |
| `Expression expected (character %d)` | Expression syntax |
| `String expected (character %d)` | String literals |
| `Number expected (character %d)` | Numeric literals |
| `Unexpected symbol '%.*s' (character %d)` | Symbol handling |
| `&& expected (character %d)` | Logical AND operator |
| `\|\| expected (character %d)` | Logical OR operator |
| `== expected (character %d)` | Equality operator |

## Keyword Categories Summary

### Confirmed (with evidence): 40+
- Access: `private`, `protected`, `public`
- Class: `sealed`, `abstract`, `modded`
- Member: `override`, `static`, `native`
- Reference: `ref`, `notnull`, `autoptr`, `weak`
- Storage: `const`, `auto`
- Parameter: `out`, `inout`
- Types: `class`, `enum`, `typedef`, `void`, `typename`
- Primitives: `int`, `float`, `string`, `bool`
- Control: `for`, `foreach`, `while`, `switch`, `case`, `return`, `if`, `else`, `break`, `continue`, `default`
- Special: `vanilla`, `this`, `super`, `thread`
- Operators: `new`
- Literals: `null`, `NULL`, `true`, `false`
- Preprocessor: `#if`, `#ifdef`, `#ifndef`
- Network: `RPC`, `replicated`

### Highly Likely (inferred):
- Preprocessor: `#else`, `#endif`, `#define`

## Not Found

No evidence for:
- Exception handling (`try`, `catch`, `throw`, `finally`) - likely not supported
- `goto` - likely not supported
- `sizeof` - no script-level evidence
- `interface` / `implements` - not found as keywords
- Lambda/closure syntax - not exposed to script
