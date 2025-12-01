# Diagnostic Patterns

All verified diagnostic patterns extracted from `ArmaReforgerWorkbenchSteamDiag.exe` (v1.6.0.76).

!!! info "Pattern Format"
    Patterns use printf-style format specifiers:

    - `%s` - string
    - `%d` - integer
    - `%u` - unsigned integer
    - `%.*s` - string with length

## Warnings

| Pattern | Notes |
|---------|-------|
| `'%s' is obsolete` | Simple deprecation |
| `'%s' is obsolete: %s` | Deprecation with reason |
| `Possible variable name conflict '%s'` | Variable shadowing |
| `Variable '%s' is not used` | Unused variable |
| `No need to use 'Cast' for up-casting` | Unnecessary cast |
| `Unsafe down-casting, use '%s.Cast' for safe down-casting` | Unsafe cast |
| `Unsafe down-casting, use proper Cast method for '%s'` | Unsafe cast variant |
| `Script variable '%s.%s': script default value overwrites value from source` | Override warning |
| `Script variable '%s.%s': using ResourceName picker with string property, use ResourceName type instead` | Type mismatch |
| `%s(%d): warning: %s` | Generic warning format |
| `%s read warning (line %d):` | File read warning |

## Hints

| Pattern | Notes |
|---------|-------|
| `Variable '%s' can be const` | Const suggestion |

## Generic Error Formats

| Pattern | Purpose |
|---------|---------|
| `%s(%d): error: %s` | Error with file/line |
| `%s read error (line %d):` | File read error |
| `Compile error` | Generic compile error |
| `Compile error: Failing item: %s` | Compile error with item |

## Type System Errors

| Pattern | Notes |
|---------|-------|
| `Cast not supported on type '%s'` | Invalid cast |
| `Excessive cast, variable '%s' already has type '%s'` | Unnecessary cast |
| `'%s' is not array` | Type mismatch |
| `'+=' etc. not supported on arrays` | Array operation error |
| `Expression cannot be converted to desired type` | Type conversion error |
| `Auto-pointer '%s' must be class-type` | Pointer type error |
| `Bad type '%s'` | Invalid type |
| `Can't compare 'void' type` | Void comparison |
| `Can't condition 'void' type` | Void conditional |

## Inheritance & Override Errors

| Pattern | Notes |
|---------|-------|
| `'%s': cannot derive from sealed type '%s'` | Sealed class inheritance |
| `'%s.%s': cannot override inherited member '%s' because it is private` | Private override |
| `'%s.%s': cannot override inherited member '%s' because it is sealed` | Sealed override |
| `Function '%s' is marked as override, but there is no function with this name in the base class` | Invalid override |
| `Function '%s' override signature conflict: differing 'static' usage` | Static override conflict |
| `Circle inheritance in class '%s'` | Circular inheritance |
| `Can't inherit class '%s'` | Inheritance error |
| `%s class should be inherited from %s` | Missing inheritance |
| `Can't find matching overload for function '%s'` | Overload not found |
| `Duplicate class name in parent class` | Duplicate class |
| `Method '%s::%s' already declared in parent class '%s'` | Duplicate method |

## Constructor & Instance Errors

| Pattern | Notes |
|---------|-------|
| `%s class needs to have a constructor with zero arguments when a class is being instantiated by serialization` | Serialization constructor |
| `%s class needs to have a constructor with zero arguments when using serialization` | Serialization constructor |
| `Can't clone class '%s', constructor is not public` | Private constructor |
| `Can't create instance of widget class '%s'` | Widget instantiation |
| `Constructor of type '%s' must not have any parameters when used in RPCs or replicated properties.` | RPC constructor |
| `Constructor '%s', argument '%s' name differs from prototype '%s'` | Argument name mismatch |
| `Constructor '%s', argument '%s' is not compatible with prototype argument type or spec '%s'` | Argument type mismatch |

## Access Modifier Errors

| Pattern | Notes |
|---------|-------|
| `Private conflicts with protected` | Access modifier conflict |
| `'this' or 'super' inside static method is not valid` | Static context error |
| `'vanilla' keyword can be used only in modded classes` | Modding keyword error |

## Assignment & Operator Errors

| Pattern | Notes |
|---------|-------|
| `Assign operator '%s' not allowed here` | Invalid assignment |
| `Assigning to value, expected local variable.` | Value assignment error |
| `Only NULL assignment is allowed` | Null-only assignment |
| `Only null assignment is allowed on plain data` | Plain data assignment |
| `Unknown operator '%s'` | Unknown operator |
| `Unexpected operator '%.*s' (character %d)` | Unexpected operator |
| `Unary operator needs to be followed by valid expression.` | Unary expression error |
| `invalid operator` | Generic operator error |

## Callback & Method Errors

| Pattern | Notes |
|---------|-------|
| `Callback method '%s' has not supported arguments!` | Callback argument error |
| `Callback method '%s' is not compatible with prototype '%s'` | Callback prototype mismatch |
| `Callback '%s' argument '%s' is not compatible ('%s' <- '%s')` | Callback argument type |
| `Calling nonexistent function on class '%s'` | Missing function |
| `Can't make callback from non-static function '%s' without instance.` | Static callback error |
| `Can't make callback from unknown method '%s'` | Unknown method callback |
| `Can't make callback on type '%s' (must be inherited from Managed).` | Managed type required |
| `Cannot create thread out of non-script function '%s'` | Thread creation error |
| `Can't apply filter on event without arguments.` | Event filter error |
| `Cannot find function '%s'` | Function not found |
| `Can't find argument '%s'` | Argument not found |
| `Cannot convert '%s%s' to '%s%s' for argument '%d' in method '%s'` | Argument conversion |
| `CallFunctionParams: Cannot convert '%s' to '%s' in argument '%s', method '%s'` | Parameter conversion |

## Null-Related Errors

| Pattern | Notes |
|---------|-------|
| `'notnull' must not be used with '%s' type` | Notnull type error |
| `Argument is null.` | Null argument |
| `Argument 'ancestor' can't be null!` | Null ancestor |
| `Argument 'child' can't be null!` | Null child |

## Attribute Validation Errors

| Pattern | Notes |
|---------|-------|
| `Attribute %s doesn't have parameter %s set up. Set it or remove it from 'Variables' category to turn it into a regular Attribute.` | Attribute parameter missing |
| `Attribute %s not in 'Variables' category. Add it or remove the use of parameters to turn it into a regular Attribute.` | Attribute category error |
| `Attribute %s has invalid type %s in it's parameters. Change it for a valid one.` | Attribute type error |
| `'%s' method from '%s' attribute params of '%s.%s' variable doesn't exist` | Attribute method missing |
| `'%s' method from '%s' attribute params of '%s.%s' variable should have only 1 parameter` | Attribute parameter count |
| `'%s' method from '%s' attribute params of '%s.%s' variable should not return any value` | Attribute return value |
| `'%s' method from '%s' attribute params of '%s.%s' variable parameter type ('%s') is not equal to the variable type ('%s')` | Attribute type mismatch |

## Template & Class Errors

| Pattern | Notes |
|---------|-------|
| `Can't compile template class '%s'` | Template compilation |
| `...while compiling template class '%s'` | Template error context |
| `Config class '%s' hasn't script declaration and can't be instantiated` | Config instantiation |
| `Engine class '%s' cannot be modded.` | Modding restriction |
| `Array initialization of non-array type '%s'` | Array init error |

## Syntax Errors

| Pattern | Notes |
|---------|-------|
| `Expected closing brace '}' (line %u).` | Missing closing brace |
| `Expected end of file after last closing brace '}' (line %u).` | Extra content after close |
| `Missing closing curly brace` | Unclosed brace |
| `Opened scope at the end of file, missing '}' ?` | EOF without closing scope |
| `Unexpected end of file` | Premature EOF |
| `Unmatched brackets detected!` | Bracket mismatch |
| `Unmatched parenthesis '%.*s' (character %d)` | Parenthesis mismatch |
| `CParser: #if[n]def expected an identifier` | Preprocessor error |
| `Expression Operator parse error` | Expression parsing error |

## Undefined/Unknown Errors

| Pattern | Notes |
|---------|-------|
| `Undefined function '%s'` | Unknown function |
| `Undefined variable` | Unknown variable |
| `Unknown class '%s'` | Unknown class |
| `Unknown type '%s'` | Unknown type |

## Return Type Errors

| Pattern | Notes |
|---------|-------|
| `Method '%s.%s' has wrong return type. Expected '%s', found '%s'.` | Return type mismatch |
| `Return type of method '%s' is not compatible` | Incompatible return |
| `Wrong usage of '%s' in method '%s.%s': the method return type must be void` | Non-void return error |
| `Wrong argument types for function '%.*s' (character %d)` | Argument type mismatch |
| `Overloaded function '%s', argument '%s' is not compatible with prototype argument type or spec '%s'` | Overload signature error |

## Static Context Errors

| Pattern | Notes |
|---------|-------|
| `Trying to access non-static member '%s' from static method '%s'` | Static accessing non-static |
| `Trying to call non-static function '%s' as static` | Non-static called as static |
| `Can't make callback from non-static function '%s' without instance.` | Callback needs instance |
| `Script called BumpMe from a static context!` | BumpMe static context error |

## RPC/Replication Errors

| Pattern | Notes |
|---------|-------|
| `Constructor of type '%s' must not have any parameters when used in RPCs or replicated properties.` | RPC constructor params |
| `RPC '%s.%s' has parameters that cannot be replicated. RPC calls will be discarded.` | Non-replicable params |
| `RPC '%s.%s' specifies default values for some of its parameters. This is not supported for RPCs.` | RPC default values |
| `Variable '%s.%s' is marked as replicated property, but it is also static. Static variable replication is not supported.` | Static replication error |

## Enum Errors

| Pattern | Notes |
|---------|-------|
| `Enum '%s' with bit flag sequence reach maximum of 32 values` | Enum value limit |
| `Enum '%s' with special sequence(linear/bit flag), can't have custom values` | Custom value restriction |
| `Only simple expressions supported in enum value '%s'` | Complex enum expression |

## Array/Index Errors

| Pattern | Notes |
|---------|-------|
| `Array bounds exceeded` | Out of bounds |
| `Array size do not match, '%s[%d]' is smaller than %s[%d]` | Array size mismatch |
| `Index out of range` | Index bounds error |
| `Index out of range (%d >= %d)` | Index with details |

## Validation System Errors

| Pattern | Notes |
|---------|-------|
| `%s: The attribute '%s' is required but missing.` | Required attribute missing |
| `%s: The content is not valid. Expected is %s.` | Content validation failure |
| `%s: The facet '%s' is not allowed on types derived from the type %s.` | Facet restriction |
| `%s: The facet '%s' is not allowed.` | Facet not allowed |
| `%sThe attribute '%s' is not allowed.` | Attribute not allowed |

## Script Compilation Messages

| Pattern | Notes |
|---------|-------|
| `Can't compile "%s" script module!` | Module compilation |
| `Can't compile "%s"!` | Generic compilation |
| `Addon cannot be packed due to failed script compilation!` | Pack failure |
| `Compilation failed for @"%s"` | Compilation failure |
| `Compiling Game scripts` | Progress message |
| `Compiling GameLib scripts` | Progress message |
