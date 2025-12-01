# Enforce Script Grammar Reference

Complete grammar and syntax documentation for Enforce Script, derived from parser error messages, AST node types, and compiler infrastructure analysis.

## Lexical Structure

### Identifiers

Identifiers follow C-like rules:
- Start with letter or underscore
- Followed by letters, digits, or underscores
- Case-sensitive
- Cannot be a keyword

**Error Evidence:**
- `Identifier expected (character %d)`
- `Expected name, not a keyword '%s'`
- `Unknown identifier '%.*s' (character %d)`

### Keywords (Reserved)

The following are reserved keywords and cannot be used as identifiers:

#### Access Modifiers
| Keyword | Purpose |
|---------|---------|
| `private` | Private access (class-only) |
| `protected` | Protected access (class + derived) |
| `public` | Public access (unrestricted) |

#### Class Modifiers
| Keyword | Purpose |
|---------|---------|
| `class` | Class definition |
| `sealed` | Prevent inheritance |
| `abstract` | Abstract class/method |
| `modded` | Modded class definition |

#### Member Modifiers
| Keyword | Purpose |
|---------|---------|
| `static` | Static member |
| `native` | Native implementation |
| `override` | Override base method |
| `const` | Constant value |
| `auto` | Auto type inference |

#### Reference Modifiers
| Keyword | Purpose |
|---------|---------|
| `ref` | Strong reference |
| `autoptr` | Auto-releasing pointer |
| `weak` | Weak reference |
| `notnull` | Non-null constraint |

#### Parameter Modifiers
| Keyword | Purpose |
|---------|---------|
| `out` | Output parameter |
| `inout` | Input/output parameter (inferred) |

#### Type Keywords
| Keyword | Purpose |
|---------|---------|
| `void` | No return type |
| `typename` | Type reference |
| `enum` | Enumeration definition |
| `typedef` | Type alias |

#### Control Flow
| Keyword | Purpose |
|---------|---------|
| `if` | Conditional branch |
| `else` | Alternative branch |
| `for` | For loop |
| `foreach` | Foreach loop |
| `while` | While loop |
| `switch` | Switch statement |
| `case` | Switch case |
| `default` | Default case |
| `break` | Exit loop/switch |
| `continue` | Skip to next iteration |
| `return` | Return from function |

#### Special Keywords
| Keyword | Purpose |
|---------|---------|
| `new` | Object instantiation |
| `this` | Current instance |
| `super` | Parent class reference |
| `vanilla` | Access vanilla (original) class in modded |
| `thread` | Thread creation |
| `null` / `NULL` | Null reference |
| `true` / `false` | Boolean literals |

### Literals

#### Numeric Literals
```
integer:    123, -456, 0xFF, 0b1010
float:      1.5, -3.14, 1e-5, 2.5f
```

**Error Evidence:**
- `Number expected (character %d)`
- `Expected numeric constant`

#### String Literals
```
"Hello, World!"
"Line with \"escaped\" quotes"
"Path\\to\\file"
```

**Error Evidence:**
- `String expected (character %d)`
- `CParser: quoted string not closed on line %d, module %s`

#### Boolean Literals
```
true
false
```

### Comments

```enforce
// Single-line comment

/* Multi-line
   comment */
```

## Operators

### Operator Precedence (Highest to Lowest)

Based on AST node types and error messages:

| Precedence | Operators | Associativity | Description |
|------------|-----------|---------------|-------------|
| 1 (highest) | `()` `[]` `.` | Left | Grouping, subscript, member access |
| 2 | `++` `--` (postfix) | Left | Postfix increment/decrement |
| 3 | `!` `-` (unary) `++` `--` (prefix) | Right | Unary operators |
| 4 | `new` `(type)` | Right | Instantiation, cast |
| 5 | `*` `/` `%` | Left | Multiplication, division, modulo |
| 6 | `+` `-` | Left | Addition, subtraction |
| 7 | `<<` `>>` | Left | Bitwise shift |
| 8 | `<` `<=` `>` `>=` | Left | Relational |
| 9 | `==` `!=` | Left | Equality |
| 10 | `&` | Left | Bitwise AND |
| 11 | `^` | Left | Bitwise XOR |
| 12 | `\|` | Left | Bitwise OR |
| 13 | `&&` | Left | Logical AND |
| 14 | `\|\|` | Left | Logical OR |
| 15 | `?:` | Right | Ternary conditional |
| 16 (lowest) | `=` `+=` `-=` `*=` `/=` `%=` etc. | Right | Assignment |

**Error Evidence:**
- `&& expected (character %d)`
- `|| expected (character %d)`
- `== expected (character %d)`
- `Unexpected operator '%.*s' (character %d)`
- `Operator '%s' is not supported by type '%s'`
- `Operator '%s' is not postfix`

### Unary Operators

| Operator | Description | AST Node |
|----------|-------------|----------|
| `!` | Logical NOT | `UnaryOp@ast@enf` |
| `-` | Negation | `UnaryOp@ast@enf` |
| `++` | Increment (prefix/postfix) | `UnaryOp@ast@enf` |
| `--` | Decrement (prefix/postfix) | `UnaryOp@ast@enf` |

**Error Evidence:**
- `Unary operator needs to be followed by valid expression.`
- `Operator '%s' is not postfix`

### Binary Operators

| Operator | Description | AST Node |
|----------|-------------|----------|
| `+` `-` `*` `/` `%` | Arithmetic | `BinaryOp@ast@enf` |
| `==` `!=` `<` `>` `<=` `>=` | Comparison | `BinaryOp@ast@enf` |
| `&&` `\|\|` | Logical | `BinaryOp@ast@enf` |
| `&` `\|` `^` `<<` `>>` | Bitwise | `BinaryOp@ast@enf` |
| `=` `+=` `-=` etc. | Assignment | `BinaryOp@ast@enf` |

**Error Evidence:**
- `Assign operator '%s' not allowed here`
- `Operator cannot work with these types`
- `'%s' not supported on 'bool'`

### Assignment Operators

```
=      // Simple assignment
+=     // Add and assign
-=     // Subtract and assign
*=     // Multiply and assign
/=     // Divide and assign
%=     // Modulo and assign
&=     // Bitwise AND and assign
|=     // Bitwise OR and assign
^=     // Bitwise XOR and assign
<<=    // Left shift and assign
>>=    // Right shift and assign
```

## Statements

### Expression Statement
```enforce
expression;
```

### Variable Declaration
```enforce
[modifiers] type name [= initializer];
```

**Modifiers:** `static`, `const`, `auto`, `ref`, `autoptr`, `weak`, `notnull`

**Examples:**
```enforce
int count = 0;
static const float PI = 3.14159;
ref MyClass instance = new MyClass();
autoptr array<int> numbers = new array<int>;
```

**Error Evidence:**
- `Variable '%s' can be const`
- `static/const variables can't be auto`
- `Variable '%s' is not strong ref (missing 'ref' keyword?)`

### If Statement
```enforce
if (condition)
    statement
[else
    statement]
```

**AST Node:** `BranchNode@ast@enf`

**Error Evidence:**
- `If statement condition always false`
- `If statement condition always true`
- `If statement without arguments.`

### For Loop
```enforce
for (init; condition; update)
    statement
```

**AST Node:** `ForLoopNode@ast@enf`

**Examples:**
```enforce
for (int i = 0; i < 10; i++)
{
    // loop body
}
```

### Foreach Loop
```enforce
foreach (element : collection)
    statement
```

**AST Node:** `ForeachLoopNode@ast@enf`

**Examples:**
```enforce
foreach (Entity entity : entities)
{
    // process entity
}
```

### While Loop
```enforce
while (condition)
    statement
```

**AST Node:** `WhileLoopNode@ast@enf`

### Switch Statement
```enforce
switch (expression)
{
    case value1:
        statements
        break;
    case value2:
        statements
        break;
    default:
        statements
        break;
}
```

**AST Nodes:** `SwitchNode@ast@enf`, `CaseNode@ast@enf`

**Error Evidence:**
- `Switch: fall through cases can't have a body`
- `Misplaced break/case/continue`

### Return Statement
```enforce
return [expression];
```

**Error Evidence:**
- `No return statement in function returning non-void '%s'`
- `return-statement with a value, in function returning 'void'`

### Break/Continue
```enforce
break;      // Exit loop or switch
continue;   // Skip to next iteration
```

**Error Evidence:**
- `Misplaced break/case/continue`

## Declarations

### Class Declaration
```enforce
[modded] [sealed] class ClassName [: BaseClass]
{
    // members
}
```

**AST Node:** `ClassDefNode@ast@enf`

**Parser Regex Evidence:** `^(\s*\bmodded\b|\s*\bsealed\b)*\s*(\bclass\b|\benum\b)+\s(\w+)`

**Examples:**
```enforce
class MyClass
{
    // members
}

sealed class FinalClass : BaseClass
{
    // cannot be inherited
}

modded class SCR_MyComponent : SCR_MyComponent
{
    // modded version
}
```

**Error Evidence:**
- `'%s': cannot derive from sealed type '%s'`
- `Sealed type '%s' can't be modded`
- `Can't inherit class '%s'`
- `%s class should be inherited from %s`

### Function Declaration
```enforce
[modifiers] returnType functionName([parameters]) [override]
{
    body
}
```

**AST Node:** `FuncDefNode@ast@enf`

**Modifiers:** `static`, `native`, `private`, `protected`, `override`, `sealed`

**Examples:**
```enforce
void DoSomething()
{
    // function body
}

static int Calculate(int a, int b)
{
    return a + b;
}

override void OnUpdate(float timeSlice)
{
    super.OnUpdate(timeSlice);
    // additional logic
}
```

**Error Evidence:**
- `Function '%s' is marked as override, but there is no function with this name in the base class`
- `Function '%s' override signature conflict: differing 'static' usage`
- `Function '%s' cannot be private/protected`
- `Overriding function '%s' but not marked as 'override'`
- `Script function cannot be native '%s'`

### Parameter Declaration
```enforce
[modifiers] type name [= default]
```

**Modifiers:** `out`, `inout`, `notnull`

**Examples:**
```enforce
void Process(int value, out int result)
{
    result = value * 2;
}

void SetEntity(notnull Entity entity)
{
    // entity is guaranteed non-null
}
```

**Error Evidence:**
- `Native functions don't support 'out' arguments '%s'`
- `inout/out/notnull can be used only on function parameters`
- `'notnull' must not be used with '%s' type`

### Enumeration Declaration
```enforce
enum EnumName
{
    VALUE1,
    VALUE2 = expression,
    VALUE3
}
```

**AST Node:** `EnumDefNode@ast@enf`

**Examples:**
```enforce
enum MyState
{
    IDLE,
    RUNNING = 1,
    PAUSED = 2,
    STOPPED
}
```

**Error Evidence:**
- `Only simple expressions supported in enum value '%s'`
- `Can't change sequence type in inherited enum`

### Typedef Declaration
```enforce
typedef ExistingType NewTypeName;
```

**AST Node:** `TypeDefNode@ast@enf`

**Error Evidence:**
- `Circle inheritance in typedef '%s'`

## Expressions

### Literal Expressions
```enforce
123              // Integer
3.14             // Float
"hello"          // String
true / false     // Boolean
null             // Null reference
```

### Identifier Expression
```enforce
variableName
ClassName.CONSTANT
```

### Member Access
```enforce
object.member
object.method(args)
ClassName.staticMember
```

### Array Access
```enforce
array[index]
matrix[row][col]
```

### Function Call
```enforce
functionName(arg1, arg2)
object.method(arg1, arg2)
```

**AST Node:** `CallOp@ast@enf`

**Error Evidence:**
- `Not enough parameters in function '%s'`
- `Wrong argument count for function '%.*s' (character %d)`
- `Wrong argument types for function '%.*s' (character %d)`

### New Expression
```enforce
new ClassName()
new ClassName(arg1, arg2)
new array<Type>
```

**AST Node:** `NewOp@ast@enf`

**Error Evidence:**
- `Can't clone class '%s', constructor is not public`

### Cast Expression
```enforce
(Type)expression
Type.Cast(expression)
```

**AST Node:** `CastNode@ast@enf`

**Error Evidence:**
- `Excessive cast, variable '%s' already has type '%s'`

### Ternary Operator
```enforce
condition ? trueExpr : falseExpr
```

### This/Super
```enforce
this.member
super.method()
```

**Error Evidence:**
- `'this' or 'super' inside static method is not valid`

## Attributes

Attributes use square bracket syntax placed before declarations.

### Syntax
```enforce
[AttributeName]
[AttributeName()]
[AttributeName(parameter)]
[AttributeName(name = value)]
[AttributeName(param1, param2)]
```

### Placement
```enforce
[Attribute("class")]
class MyClass
{
    [Attribute("field")]
    int field;

    [Attribute("method")]
    void Method()
    {
    }
}
```

**Known Attributes:**
- `[EventAttribute]` - Event method marker
- `[ReceiverAttribute]` - Receiver method marker

**Error Evidence:**
- `Method '%s.%s' is not marked with the [EventAttribute] attribute.`
- `Method '%s.%s' is not marked with the [ReceiverAttribute] attribute.`

## Type System

### Primitive Types
| Type | Description |
|------|-------------|
| `int` | 32-bit signed integer |
| `float` | 32-bit floating point |
| `bool` | Boolean (true/false) |
| `string` | Text string |
| `void` | No type/return |

### Complex Types
| Type | Description |
|------|-------------|
| `vector` | 3D vector (x, y, z) |
| `array<T>` | Dynamic array |
| `set<T>` | Unique collection |
| `map<K,V>` | Key-value mapping |
| `ResourceName` | Resource path |

### Reference Types
```enforce
ref MyClass            // Strong reference
autoptr MyClass        // Auto-releasing pointer
weak MyClass          // Weak reference
```

**Error Evidence:**
- `autoptr/ref in template is not supported on non-managed class '%s'`
- `Script variable '%s.%s': using weak pointer to store object, use 'ref' for strong reference`

### Type Constraints
```enforce
notnull Type          // Must not be null
```

## Preprocessor Directives

### Conditional Compilation
```enforce
#ifdef IDENTIFIER
    // code when defined
#endif

#ifndef IDENTIFIER
    // code when not defined
#endif

#if condition
    // conditional code
#else
    // alternative code
#endif
```

**Error Evidence:**
- `CParser: #if[n]def expected an identifier`

### Other Directives (Inferred)
```enforce
#define IDENTIFIER value
#include "file"
```

## RPC and Replication

### RPC Declaration
```enforce
[RPC] void RemoteMethod(params)
```

**Error Evidence:**
- `RPC '%s.%s' has parameters that cannot be replicated`

### Replicated Variables
```enforce
[Replicated] int replicatedVar;
```

**Error Evidence:**
- `Variable '%s.%s' is marked as replicated property`

## Threading

```enforce
thread DoAsyncWork();
```

**Error Evidence:**
- `Cannot create thread out of non-script function '%s'`

## Error Messages Reference

### Parser Errors (Character Position)
| Message | Meaning |
|---------|---------|
| `Identifier expected (character %d)` | Expected identifier at position |
| `Expression expected (character %d)` | Expected expression at position |
| `String expected (character %d)` | Expected string literal |
| `Number expected (character %d)` | Expected numeric literal |
| `End expected (character %d)` | Expected end of statement/block |
| `&& expected (character %d)` | Expected logical AND |
| `\|\| expected (character %d)` | Expected logical OR |
| `== expected (character %d)` | Expected equality operator |
| `Unexpected operator '%.*s' (character %d)` | Invalid operator |
| `Unexpected symbol '%.*s' (character %d)` | Unexpected character |
| `Missing operand (character %d)` | Missing operand in expression |
| `Unmatched parenthesis '%.*s' (character %d)` | Unclosed parenthesis |
| `Unmatched quote '%.*s' (character %d)` | Unclosed string |

### Semantic Errors
| Message | Meaning |
|---------|---------|
| `Expected name, not a keyword '%s'` | Keyword used as identifier |
| `Modifiers are not allowed` | Invalid modifier usage |
| `Variable '%s' can be const` | Suggestion to use const |
| `Forward declarations are deprecated` | Use full declarations |
| `Broken expression (missing ';'?)` | Likely missing semicolon |

## Grammar Summary (BNF-like)

```
program          ::= declaration*

declaration      ::= classDecl | enumDecl | typedefDecl | functionDecl

classDecl        ::= classModifier* 'class' IDENTIFIER [':' IDENTIFIER] '{' memberDecl* '}'
classModifier    ::= 'modded' | 'sealed'

enumDecl         ::= 'enum' IDENTIFIER '{' enumValue (',' enumValue)* '}'
enumValue        ::= IDENTIFIER ['=' expression]

typedefDecl      ::= 'typedef' type IDENTIFIER ';'

functionDecl     ::= modifier* type IDENTIFIER '(' paramList? ')' ['override'] block

paramList        ::= param (',' param)*
param            ::= paramModifier* type IDENTIFIER ['=' expression]
paramModifier    ::= 'out' | 'inout' | 'notnull'

memberDecl       ::= fieldDecl | functionDecl
fieldDecl        ::= modifier* type IDENTIFIER ['=' expression] ';'

modifier         ::= 'static' | 'const' | 'auto' | 'ref' | 'autoptr' | 'weak' | 'notnull'
                   | 'private' | 'protected' | 'public' | 'native' | 'override' | 'sealed'

type             ::= primitiveType | IDENTIFIER ['<' typeArgs '>']
primitiveType    ::= 'void' | 'int' | 'float' | 'bool' | 'string' | 'vector'
typeArgs         ::= type (',' type)*

block            ::= '{' statement* '}'

statement        ::= varDecl
                   | ifStmt
                   | forStmt
                   | foreachStmt
                   | whileStmt
                   | switchStmt
                   | returnStmt
                   | breakStmt
                   | continueStmt
                   | expressionStmt
                   | block

varDecl          ::= modifier* type IDENTIFIER ['=' expression] ';'
ifStmt           ::= 'if' '(' expression ')' statement ['else' statement]
forStmt          ::= 'for' '(' [forInit] ';' [expression] ';' [expression] ')' statement
foreachStmt      ::= 'foreach' '(' type IDENTIFIER ':' expression ')' statement
whileStmt        ::= 'while' '(' expression ')' statement
switchStmt       ::= 'switch' '(' expression ')' '{' caseClause* '}'
caseClause       ::= ('case' expression | 'default') ':' statement*
returnStmt       ::= 'return' [expression] ';'
breakStmt        ::= 'break' ';'
continueStmt     ::= 'continue' ';'
expressionStmt   ::= expression ';'

expression       ::= assignmentExpr
assignmentExpr   ::= ternaryExpr (assignOp assignmentExpr)?
ternaryExpr      ::= logicalOrExpr ('?' expression ':' ternaryExpr)?
logicalOrExpr    ::= logicalAndExpr ('||' logicalAndExpr)*
logicalAndExpr   ::= bitwiseOrExpr ('&&' bitwiseOrExpr)*
bitwiseOrExpr    ::= bitwiseXorExpr ('|' bitwiseXorExpr)*
bitwiseXorExpr   ::= bitwiseAndExpr ('^' bitwiseAndExpr)*
bitwiseAndExpr   ::= equalityExpr ('&' equalityExpr)*
equalityExpr     ::= relationalExpr (('==' | '!=') relationalExpr)*
relationalExpr   ::= shiftExpr (('<' | '>' | '<=' | '>=') shiftExpr)*
shiftExpr        ::= additiveExpr (('<<' | '>>') additiveExpr)*
additiveExpr     ::= multiplicativeExpr (('+' | '-') multiplicativeExpr)*
multiplicativeExpr ::= unaryExpr (('*' | '/' | '%') unaryExpr)*
unaryExpr        ::= ('!' | '-' | '++' | '--') unaryExpr | postfixExpr
postfixExpr      ::= primaryExpr (memberAccess | arrayAccess | functionCall | '++' | '--')*
memberAccess     ::= '.' IDENTIFIER
arrayAccess      ::= '[' expression ']'
functionCall     ::= '(' [argList] ')'
argList          ::= expression (',' expression)*
primaryExpr      ::= literal | IDENTIFIER | '(' expression ')' | newExpr | castExpr | 'this' | 'super'
newExpr          ::= 'new' type ['(' [argList] ')']
castExpr         ::= '(' type ')' unaryExpr

literal          ::= INTEGER | FLOAT | STRING | 'true' | 'false' | 'null'
assignOp         ::= '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '&=' | '|=' | '^=' | '<<=' | '>>='

attribute        ::= '[' IDENTIFIER ['(' attrArgs ')'] ']'
attrArgs         ::= attrArg (',' attrArg)*
attrArg          ::= expression | IDENTIFIER '=' expression
```

## Best Practices

1. **Use `ref` for class references** - Prevents dangling pointers
2. **Mark variables `const` when possible** - Compiler will suggest this
3. **Use `override` explicitly** - Prevents accidental shadowing
4. **Avoid forward declarations** - They are deprecated
5. **Use `notnull` on parameters** - Catches null errors at compile time
6. **Prefer `foreach` over indexed `for`** - Cleaner and safer
