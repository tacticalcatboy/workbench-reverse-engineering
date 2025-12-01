# Type System

Built-in types discovered through type traits and error messages.

## Primitive Types

| Type | Evidence |
|------|----------|
| `int` | `IntTrait` found in strings |
| `float` | `FloatTrait` found in strings |
| `bool` | `'%s' not supported on 'bool'` |
| `string` | `TString@enf`, `StringTrait` |
| `void` | `the method return type must be void` |

## Vector Types

| Type | Evidence |
|------|----------|
| `Vector2` | `VectorTrait` (2D vector) |
| `Vector3` | `VectorTrait` (3D vector) |
| `Vector4` | `VectorTrait` (4D vector) |

## Special Types

| Type | Evidence |
|------|----------|
| `typename` | `Static array of 'typename' types is not supported` |
| `ResourceName` | `ResourceName@enf`, `using ResourceName picker with string property, use ResourceName type instead` |

## Memory Management Types

| Type | Purpose | Evidence |
|------|---------|----------|
| `ref` | Strong reference | `Variable '%s' is not strong ref (missing 'ref' keyword?)` |
| `RefPtr<T>` | Strong reference pointer | Found in strings |
| `WeakPtr<T>` | Weak reference pointer | Found in strings |
| `ManagedInstance` | Managed memory base | `ManagedInstance@enf` |
| `Managed` | Managed base class | `must be inherited from Managed` |

## Array Types

Arrays are indicated by `[]` syntax:

```
Type[]           // Array of Type
Type[size]       // Fixed-size array (likely)
```

Evidence:
- `'%s' is not array`
- `'+=' etc. not supported on arrays`
- `Array bounds exceeded`
- `Array size do not match, '%s[%d]' is smaller than %s[%d]`

## Type Components

### VarType@enf
Main type representation class.

### TypeNode@ast@enf
AST node for type references.

### Type Traits
- `IntTrait`
- `FloatTrait`
- `StringTrait`
- `VectorTrait`

## Casting

### Safe Casting
```
TargetType.Cast(source)
```

Evidence:
- `Unsafe down-casting, use '%s.Cast' for safe down-casting`
- `No need to use 'Cast' for up-casting`

### Cast Errors

| Error | Meaning |
|-------|---------|
| `Cast not supported on type '%s'` | Type cannot be cast |
| `Excessive cast, variable '%s' already has type '%s'` | Unnecessary cast |
| `No need to use 'Cast' for up-casting` | Upcast doesn't need Cast |

## Null Handling

| Feature | Evidence |
|---------|----------|
| `null` / `NULL` | `Only NULL assignment is allowed` |
| `notnull` modifier | `'notnull' must not be used with '%s' type` |

## Type Inference

Auto-pointer types must be class types:
- `Auto-pointer '%s' must be class-type`

## Unknown

- Complete list of primitive types
- Generic/template syntax details
- Type aliases/typedef support
- Tuple types (if any)
- Optional/nullable types
