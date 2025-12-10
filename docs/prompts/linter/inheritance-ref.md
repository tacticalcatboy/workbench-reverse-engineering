# Enforce Script Inheritance Reference

Class hierarchy and inheritance rules for Arma Reforger / Enfusion.

---

## Key Inheritance Chains

### Entity Hierarchy

```
Managed
└── IEntity
    └── GenericEntity
        ├── PawnEntity
        │   └── CharacterEntity
        ├── BaseWeatherManagerEntity
        ├── CinematicEntity
        ├── CrossroadEntity
        └── DecalEntity
```

### Component Hierarchy

```
(none - root class)
└── GenericComponent
    ├── AnimationControllerComponent
    ├── AnimationPlayerComponent
    ├── BaseMaterialParamsComponent
    ├── BaseProcAnimComponent
    ├── BaseRplComponent
    │   └── RplComponent
    ├── BaseSoundComponent
    │   └── CharacterSndComponent
    ├── CharacterAnimGraphComponent
    ├── CharacterFSMComponent
    ├── CharacterMovementComponent
    └── (1,200+ more component classes)
```

### Widget Hierarchy

```
Managed
└── ScriptedWidgetEventHandler
    ├── ScriptedWidgetComponent
    └── Widget
        ├── CanvasWidgetBase
        │   └── CanvasWidget
        ├── BlurWidget
        ├── ContentWidget
        └── UIWidget
            ├── BaseListboxWidget
            ├── BasicGraphWidget
            ├── ButtonWidget
            ├── CheckBoxWidget
            ├── EditBoxWidget
            └── TextWidget
```

### Game Mode Hierarchy

```
BaseGameMode
└── SCR_BaseGameMode
    ├── SCR_CampaignGameMode
    ├── SCR_ConflictGameMode
    └── (other game modes)
```

---

## Root Classes (No Parent)

Classes that don't extend anything - these are inheritance roots:

### Core Types
- `bool`, `int`, `float`, `string`, `func`

### System Classes
- `ActionManager` - Input action system
- `AudioSystem` - Audio playback
- `BackendApi` - Backend services
- `Debug` - Debug utilities
- `DiagMenu` - Diagnostic menu
- `FileIO` - File operations
- `Game` - Game instance
- `Managed` - Base managed object

### Component Base
- `GenericComponent` - All components derive from this
- `GenericComponentClass` - Component class descriptor

### Data Classes
- `Attribute` - Attribute decorator base
- `BaseContainer` - Data container
- `EntityPrefabData` - Entity prefab data
- `EntitySpawnParams` - Spawn parameters

### Events
- `Event` - Event base class
- `CallbackContext` - Callback context
- `CallbackMethod` - Callback method wrapper

---

## Common Inheritance Patterns

### Component Pattern

All gameplay components extend `GenericComponent`:

```enforce
class MyComponent extends GenericComponent
{
    override void EOnInit(IEntity owner)
    {
        // Initialization
    }
}
```

### ScriptComponent Pattern (SCR_)

Arma Reforger scripted components:

```enforce
class SCR_MyComponent extends ScriptComponent
{
    // ScriptComponent extends GenericComponent
}
```

### Widget Handler Pattern

UI event handlers:

```enforce
class MyWidgetHandler extends ScriptedWidgetEventHandler
{
    override bool OnClick(Widget w, int x, int y, int button)
    {
        return true; // handled
    }
}
```

### Entity Class Descriptor Pattern

Every entity/component has a paired "Class" descriptor:

```enforce
// Entity class
class MyEntity extends GenericEntity { }

// Paired descriptor (auto-generated or manual)
class MyEntityClass extends GenericEntityClass { }
```

---

## Modded Class Pattern

Extend existing classes with `modded`:

```enforce
modded class SCR_CharacterControllerComponent
{
    override void EOnInit(IEntity owner)
    {
        super.EOnInit(owner);  // Call original
        // Add your modifications
    }
}
```

Access original implementation with `vanilla`:

```enforce
modded class SomeClass
{
    void MyMethod()
    {
        vanilla.SomeMethod();  // Call unmodded version
    }
}
```

---

## Class Modifiers

### sealed

Class cannot be extended:

```enforce
sealed class FinalClass { }

// ERROR: class 'MyClass' cannot extend sealed class 'FinalClass'
class MyClass extends FinalClass { }
```

### abstract (implied)

Classes with abstract methods must be extended:

```enforce
class AbstractBase
{
    void AbstractMethod();  // No implementation = abstract
}

// Must override AbstractMethod
class ConcreteClass extends AbstractBase
{
    override void AbstractMethod()
    {
        // Implementation required
    }
}
```

---

## Key Inheritance Rules

1. **Single Inheritance Only**
   - Classes can only extend one parent
   - No multiple inheritance

2. **Override Required**
   - Must use `override` keyword when reimplementing parent methods
   - Compiler error: "method '%s' cannot override, not marked as 'override'"

3. **sealed Methods**
   - Some methods are `sealed` and cannot be overridden
   - Compiler error: "method '%s' cannot override sealed method"

4. **super Calls**
   - Use `super.MethodName()` to call parent implementation
   - Critical for EOn* event handlers

5. **Circular Inheritance Forbidden**
   - A extends B extends C extends A is invalid
   - Compiler error: "Circular class inheritance"

---

## Component Type Registration

Components register with paired *Class descriptor:

```enforce
[ComponentEditorProps(category: "Components")]
class MyComponentClass : GenericComponentClass { }

class MyComponent : GenericComponent
{
    // Implementation
}
```

---

## Valid Base Classes for Custom Code

### For Components
- `GenericComponent` - Direct component
- `ScriptComponent` - Higher-level scripted component
- `ScriptedWidgetComponent` - UI component

### For Entities
- `GenericEntity` - Basic entity
- `PawnEntity` - Controllable entity

### For UI
- `ScriptedWidgetEventHandler` - UI event handling
- `MenuBase` - Menu screens
- `DialogUI` - Dialog boxes

### For Game Logic
- `ScriptedState` - State machine states
- `ScriptedBehavior` - AI behaviors

---

*Data extracted from Arma Reforger API inheritance structure.*
