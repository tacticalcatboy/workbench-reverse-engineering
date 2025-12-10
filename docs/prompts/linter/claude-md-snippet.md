# CLAUDE.md Snippet for Enforce Script Projects

Copy the section below into your project's `CLAUDE.md` file to enable AI-powered linting.

---

## Snippet (Copy Below This Line)

```markdown
# Enforce Script Linting

When reviewing `.c` files in this project, apply Enforce Script validation rules.

## Language Overview

Enforce Script is a C-like language for Arma Reforger modding:
- Single inheritance only (`class Foo extends Bar`)
- No exceptions (no try/catch)
- Reference types: `ref` (strong), `autoptr` (auto-release), `weak` (may become null), `notnull` (compile-time null check)
- `modded` keyword extends vanilla classes, use `super` to call original
- Attributes use `[Attribute]` syntax before declarations

## Keywords

**Reserved:** class, sealed, modded, abstract, private, protected, public, static, native, override, const, auto, ref, autoptr, weak, notnull, out, inout, void, typename, enum, typedef, if, else, for, foreach, while, switch, case, default, break, continue, return, new, this, super, vanilla, thread, null, NULL, true, false

## Type Conversions

**Implicit (allowed):** int->float, int->bool, float->bool, string->int, string->float, derived->base

**Explicit required:** int->string (`.ToString()`), float->string (`.ToString()`), base->derived (`.Cast()`)

## Common Errors to Catch

### ERROR (Will fail compilation)

| Pattern | Issue |
|---------|-------|
| Missing `override` | `Overriding function 'X' but not marked as 'override'` |
| Event overloading | `Overloading event 'EOnInit' is not allowed` - events can't have different signatures |
| Unsafe down-casting | `Unsafe down-casting, use 'Type.Cast' for safe down-casting` |
| No null check after FindComponent | Component may not exist, always check before use |
| Missing `super` call in modded | `modded class` should call `super.Method()` to preserve behavior |
| Sealed inheritance | Cannot extend `sealed` class |
| Static mismatch on override | Override cannot change static/non-static |
| Missing SetEventMask | `EOnFrame`/`EOnContact` require `SetEventMask(owner, EntityEvent.FRAME)` etc |
| Private method access | Cannot call `private` method from outside class |
| Int to string | `Incompatible parameter '42'` - use `.ToString()` |

### WARNING (Bad practice)

| Pattern | Issue |
|---------|-------|
| Unused variable | `Variable '%s' is not used` |
| Can be const | Variable never modified, mark `const` |
| Weak reference storage | Using `weak` to store object that may be GC'd, use `ref` |
| Missing RplRpc attribute | RPC method without `[RplRpc(...)]` won't replicate |

## Correct Patterns

### Component Access
```enforce
// CORRECT
SCR_InventoryStorageManagerComponent inv;
inv = SCR_InventoryStorageManagerComponent.Cast(FindComponent(SCR_InventoryStorageManagerComponent));
if (inv)
    inv.DoSomething();

// WRONG - no cast (triggers "Unsafe down-casting" error)
SCR_InventoryStorageManagerComponent inv = FindComponent(SCR_InventoryStorageManagerComponent);

// WRONG - no null check
inv.DoSomething();  // Crash if component doesn't exist
```

### Event Handlers
```enforce
// CORRECT
class MyComponent extends ScriptComponent
{
    override void EOnInit(IEntity owner)
    {
        SetEventMask(owner, EntityEvent.FRAME);  // Enable EOnFrame
    }

    override void EOnFrame(IEntity owner, float timeSlice)
    {
        // Called every frame
    }
}

// WRONG - missing override keyword
void EOnInit(IEntity owner)  // Won't be called!

// WRONG - missing SetEventMask
override void EOnFrame(IEntity owner, float timeSlice)  // Never called without SetEventMask
```

### Modded Classes
```enforce
// CORRECT
modded class SCR_CharacterControllerComponent
{
    override void EOnInit(IEntity owner)
    {
        super.EOnInit(owner);  // Preserve original behavior
        // Your additions here
    }
}

// WRONG - not calling super breaks original functionality
modded class SCR_CharacterControllerComponent
{
    override void EOnInit(IEntity owner)
    {
        // Original EOnInit never runs!
    }
}
```

### RPC Methods
```enforce
// CORRECT
[RplRpc(RplChannel.Reliable, RplRcver.Server)]
void RpcDoAction_S(int param)
{
    // Server executes this
}

// WRONG - missing attribute
void RpcDoAction_S(int param)  // Won't replicate!
```

## Review Format

When reviewing code, report issues as:

```
ERROR: [issue] at line X
- Explanation
- Fix: [code example]

WARNING: [issue] at line X
- Explanation
- Suggestion: [improvement]
```

## Key Classes

- **GenericComponent** / **ScriptComponent** - Component base classes
- **IEntity** / **GenericEntity** - Entity base classes
- **Widget** - UI base class
- **Managed** - Root class for garbage-collected objects

## Event Masks (for SetEventMask)

- `EntityEvent.FRAME` - Enable EOnFrame
- `EntityEvent.POSTFRAME` - Enable EOnPostFrame
- `EntityEvent.INIT` - Enable EOnInit
- `EntityEvent.CONTACT` - Enable EOnContact
- `EntityEvent.TOUCH` - Enable EOnTouch
```

---

## Usage

1. Copy the snippet above into your project's `CLAUDE.md`
2. Claude will automatically apply these rules when reviewing `.c` files
3. Ask Claude to "review this code" or "check for errors"

## Full Documentation

For complete validation rules, see:
- `data/validation/tokens.json` - All keywords and operators
- `data/validation/grammar-rules.json` - Full BNF grammar
- `data/validation/type-rules.json` - Type system rules
- `data/validation/error-patterns.json` - All 50+ error patterns
