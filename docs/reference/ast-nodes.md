# AST Node Types

Complete AST (Abstract Syntax Tree) node hierarchy discovered in the `ast@enf` namespace.

## Node Hierarchy

```
SyntaxTreeNodeBase@ast@enf
├── Node@ast@enf (base)
├── LeafNode@ast@enf (terminal)
├── BranchNode@ast@enf (conditional)
├── ListNode@ast@enf (sequence)
├── ExpressionNode@ast@enf
├── StatementNode@ast@enf
├── ClassDefNode@ast@enf
├── FuncDefNode@ast@enf
├── EnumDefNode@ast@enf
├── TypeDefNode@ast@enf
├── TypeNode@ast@enf
├── VarNode@ast@enf
├── CastNode@ast@enf
├── CaseNode@ast@enf
├── SwitchNode@ast@enf
├── ForLoopNode@ast@enf
├── ForeachLoopNode@ast@enf
├── WhileLoopNode@ast@enf
└── CommandNode@ast@enf
```

## Node Descriptions

### Base Nodes

| Node | Purpose |
|------|---------|
| `SyntaxTreeNodeBase` | Abstract base for all AST nodes |
| `Node` | Generic node class |
| `LeafNode` | Terminal nodes (literals, identifiers) |
| `BranchNode` | Conditional branches (if/else) |
| `ListNode` | Sequences of nodes |

### Definition Nodes

| Node | Purpose |
|------|---------|
| `ClassDefNode` | Class definition |
| `FuncDefNode` | Function/method definition |
| `EnumDefNode` | Enumeration definition |
| `TypeDefNode` | Type definition/alias |

### Expression Nodes

| Node | Purpose |
|------|---------|
| `ExpressionNode` | Generic expression |
| `TypeNode` | Type reference |
| `VarNode` | Variable reference |
| `CastNode` | Type cast expression |

### Statement Nodes

| Node | Purpose |
|------|---------|
| `StatementNode` | Generic statement |
| `CommandNode` | Command/directive |

### Control Flow Nodes

| Node | Purpose |
|------|---------|
| `SwitchNode` | Switch statement |
| `CaseNode` | Case clause in switch |
| `ForLoopNode` | For loop |
| `ForeachLoopNode` | Foreach loop |
| `WhileLoopNode` | While loop |

## Implications

### Language Features

The AST structure confirms:

1. **Class-based OOP** - `ClassDefNode` for class definitions
2. **Functions/Methods** - `FuncDefNode` for function definitions
3. **Enumerations** - `EnumDefNode` for enum definitions
4. **Type aliases** - `TypeDefNode` for type definitions
5. **Multiple loop types** - for, foreach, while
6. **Switch statements** - switch/case support
7. **Type casting** - explicit cast operations

### Missing Nodes

Not found (may exist under different names):
- Try/catch nodes (exception handling)
- Lambda/closure nodes
- Interface definition nodes
- Namespace nodes
- Import/include nodes

## Parser Methods

Related parser methods found in `CCompiler`:

| Method | Purpose |
|--------|---------|
| `ParseFunctionCallSt@CCompiler@enf` | Parse function calls |
| `ParseArrayCustomClassSt@CCompiler@enf` | Parse array with custom class |
| `ParseStatementsBodySt@CCompiler@enf` | Parse statement body |
