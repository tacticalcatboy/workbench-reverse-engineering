# Class Hierarchy

Class inheritance relationships, composition patterns, and module dependencies in Enforce Script.

## Core Hierarchies

### Entity Hierarchy

```
Object (root - native)
└── Managed (garbage-collected base)
    └── IEntity (interface)
        └── GenericEntity@gamelib
            ├── ScriptedGameTriggerEntity@gamecode
            ├── AIComponentEntity@ailib
            ├── BaseWeatherManagerEntity
            ├── Character entities
            ├── Vehicle entities
            └── ... (spawnable game entities)
```

**Evidence:** `Game::SpawnEntity: Class must inherits from GenericEntity!`

### Component Hierarchy

```
GenericComponent@gamelib (base component)
├── ScriptComponent@gamelib (scripted components)
└── Native components:
    ├── ActionsPerformerComponent@gamecode
    ├── CharacterControllerComponent@gamecode
    ├── CharacterAnimationComponent@gamecode
    ├── CharacterMovementComponent@gamelib
    ├── CharacterCommandHandlerComponent@gamecode
    ├── InventoryStorageManagerComponent@gamecode
    ├── BaseWeaponManagerComponent@gamecode
    ├── DamageManagerComponent@gamecode
    ├── BaseLightManagerComponent@gamecode
    ├── HitZoneContainerComponent@gamecode
    ├── CompartmentAccessComponent@gamecode
    ├── VehicleControllerComponent@gamecode
    ├── TurretControllerComponent@gamecode
    ├── FactionAffiliationComponent@gamecode
    ├── RplComponent@gamecode (replication)
    ├── SignalsManagerComponent@gamecode
    ├── AIBehaviorTreeComponent@ailib
    ├── AIComponent@ailib
    └── ... (100+ component types)
```

**Evidence:** `Component Class '%s' must inherit from '%s'`

### AI Hierarchy

```
AIAgent (AI entity base)
├── AIGroup
│   └── AIGroupMovementComponent requires AIGroup inheritance
└── AIOrder (order base class)
    └── Custom orders must inherit from AIOrder
```

**Evidence:**
- `Wrong prefab set to spawn, not inheriting from AIAgent. Prefab: %s`
- `AIGroupMovementComponent can only be a component of an Entity inheriting from AIGroup`
- `Class name with base class of AIOrder`

### Manager Class Pattern

Common manager classes discovered across namespaces:

| Manager | Namespace | Purpose |
|---------|-----------|---------|
| `EntityManager` | `enf`, `gamelib` | Entity lifecycle |
| `InputManager` | `gamelib` | Input handling |
| `MenuManager` | `gamelib` | Menu system |
| `ActionManager` | `gamelib` | Action system |
| `CameraManager` | `gamecode` | Camera control |
| `PlayerManager` | `gamecode` | Player management |
| `SaveGameManager` | `gamecode` | Save/load |
| `MissionManager` | `gamecode` | Mission handling |
| `ResourceManager` | `enf` | Resource loading |
| `PerceptionManager` | `gamecode` | AI perception |
| `FactionManager` | `gamecode` | Faction system |
| `WeatherManager` | `enf` | Weather system |
| `PhysicsManager` | `enf` | Physics engine |
| `PathManager` | `ailib` | AI pathfinding |
| `BackendManager` | `online@gamelib` | Backend services |
| `BTManager` | `bt` | Behavior trees |

## Inheritance Requirements

### Required Base Classes

| Context | Required Base Class | Evidence |
|---------|--------------------| ---------|
| Entity spawning | `GenericEntity` | `Game::SpawnEntity: Class must inherits from GenericEntity!` |
| Components | `GenericComponent` or specific base | `Component Class '%s' must inherit from '%s'` |
| Entities | Specific entity base | `Entity Class '%s' must inherit from '%s'` |
| Loading screens | `BaseLoadingAnim` | `Script class must be inherited from BaseLoadingAnim and be in GameLib script module` |
| Callbacks | `Managed` | `Can't make callback on type '%s' (must be inherited from Managed)` |
| AI agents | `AIAgent` | `Wrong prefab set to spawn, not inheriting from AIAgent` |
| AI groups | `AIGroup` | `AIGroupMovementComponent can only be a component of an Entity inheriting from AIGroup` |
| Magazine configs | `MagazineConfig` | `MagazineConfig::ReadMagazineConfig cannot read resource '%s', it does not inherit from 'MagazineConfig' class!` |
| Mission headers | `MissionHeader` | `MissionHeader::ReadMissionHeader cannot read resource '%s', it does not inherit from 'MissionHeader' class!` |
| Replication | Native Item type | `IReplication::BumpMe::Error: Script called BumpMe from item without layout! This likely means that its class is not derived from native Item type that supports replication` |
| Session callbacks | `RplSessionCallbacks` | `Callback class is not derived from RplSessionCallbacks class!` |
| Test classes | `TestBase` | `TestRegistrationError: Class with Test(...) attribute is not derived from TestBase!` |

### Inheritance Constraints

| Constraint | Error Message |
|------------|--------------|
| Circular inheritance | `Circle inheritance in class '%s'` |
| Circular enum inheritance | `Circle inheritance in enum '%s'` |
| Circular typedef | `Circle inheritance in typedef '%s'` |
| Inheritance blocked | `Can't inherit class '%s'` |
| Invalid inheritance | `Invalid inheritance, '%s' must inherit from '%s'` |

## Sealed Classes (Cannot Extend)

Sealed classes cannot be inherited from or modded:

| Error Message | Meaning |
|---------------|---------|
| `'%s': cannot derive from sealed type '%s'` | Cannot create subclass of sealed type |
| `'%s.%s': cannot override inherited member '%s' because it is sealed` | Cannot override sealed method |
| `Sealed type '%s' can't be modded` | Modded classes cannot extend sealed types |

**Usage:** The `sealed` modifier prevents inheritance:
```csharp
sealed class FinalClass { }  // Cannot be extended
```

## Abstract Classes (Must Extend)

Abstract classes cannot be instantiated directly:

| Error Message | Meaning |
|---------------|---------|
| `Requesting creation of abstract system %s, but abstract systems cannot be created.` | Cannot instantiate abstract systems |

**Usage:** The `abstract` modifier requires subclassing:
```csharp
abstract class BaseSystem { }  // Must be subclassed
class ConcreteSystem : BaseSystem { }  // Valid
```

## Override Requirements

### Override Rules

| Error Message | Meaning |
|---------------|---------|
| `Function '%s' is marked as override, but there is no function with this name in the base class` | No base method to override |
| `Overriding function '%s' but not marked as 'override'` | Missing override keyword |
| `'%s.%s': cannot override inherited member '%s' because it is private` | Cannot override private methods |
| `'%s.%s': cannot override inherited member '%s' because it is sealed` | Cannot override sealed methods |
| `Function '%s' override signature conflict: differing 'static' usage` | Static modifier mismatch |

### Override Syntax

```csharp
class BaseClass
{
    void Method() { }
}

class DerivedClass : BaseClass
{
    override void Method() { }  // Correct - override keyword required
}
```

## Common Composition Patterns

### Character Entity Composition

A typical character entity contains these components (from RPC analysis):

```
Character (GenericEntity)
├── CharacterControllerComponent (control input)
├── CharacterAnimationComponent (animation state)
├── CharacterCommandHandlerComponent (command processing)
├── CharacterMovementComponent (physics movement)
├── CharacterVicinityComponent (nearby entity detection)
├── CharacterIdentityComponent (identity/appearance)
├── InventoryStorageManagerComponent (inventory)
├── DamageManagerComponent (health/damage)
├── HitZoneContainerComponent (hitboxes)
├── BaseWeaponManagerComponent (weapons)
├── FactionAffiliationComponent (faction)
├── CompartmentAccessComponent (vehicle access)
├── RplComponent (replication)
└── AIComponent (AI control - when AI-controlled)
```

### Vehicle Entity Composition

```
Vehicle (GenericEntity)
├── VehicleControllerComponent (driver input)
├── VehicleAnimationComponent (animation)
├── BaseCompartmentManagerComponent (seats/compartments)
├── TurretControllerComponent (turret control)
├── DamageManagerComponent (damage)
├── HitZoneContainerComponent (hitboxes)
├── BaseLightManagerComponent (lights)
├── NwkMovementComponent (network movement)
│   ├── NwkCarMovementComponent
│   ├── NwkHeliMovementComponent
│   └── NwkTrackedMovementComponent
└── RplComponent (replication)
```

### Component Discovery Methods

| Method | Purpose |
|--------|---------|
| `FindComponent` | Find component by type on entity |
| `FindComponents` | Find all components of type |
| `FindComponentInParentContainer` | Search parent containers |
| `GetComponent` | Get component reference |
| `GetComponentCount` | Count components |
| `GetOwner` / `GetOwnerEntity` | Get owning entity |

## Module Dependencies

### Namespace Hierarchy

Based on class registration patterns:

```
enf (Engine core)
├── Audio (dsp@audio@enf)
├── Physics
├── Rendering
├── Entity management
├── Resource system
└── Base scripting

gamelib (Game library) - depends on enf
├── Entities
├── Components (GenericComponent, ScriptComponent)
├── Input system
├── Menu system
├── Animation system
├── Cinematic system
├── Online/backend (online@gamelib)
└── Sound (snd@gamelib)

gamecode (Game-specific) - depends on gamelib
├── Character systems
├── Vehicle systems (vhc@gamecode)
├── Weapon systems
├── AI systems
├── Inventory
├── Faction system
└── Game modes

ailib (AI library) - depends on gamelib
├── Behavior trees
├── Pathfinding
├── Road network (roadnetwork@ailib)
└── AI components

bt (Behavior tree) - AI subsystem
└── BTManager, behavior nodes

nm (Navmesh) - Navigation
└── Pathfinding infrastructure
```

### Module Registration

Script classes are registered per module:

```
RegisterScriptClasses@MenuManager@gamelib - Registers menu classes
GameLib script module - Contains BaseLoadingAnim
```

**Evidence:** `Script class handling initial splash screen. Must be inherited from BaseLoadingAnim and be in GameLib script module.`

## Interface-like Classes

Classes starting with 'I' that define contracts:

| Interface | Purpose |
|-----------|---------|
| `IEntity` | Entity interface |
| `IEntitySource` | Entity data source |
| `IEntityComponentSource` | Component data source |
| `IReplication` | Replication interface |
| `IFuncManager` | Function manager interface |
| `IKeyBindingStack` | Input binding interface |

**Note:** Enforce Script does not have formal `interface` keyword - these are abstract base classes following the 'I' prefix convention.

## Base Class Patterns

### DeclareObjectBaseClass Pattern

The `DeclareObjectBaseClass` template is used to declare base classes for the object system:

```cpp
DeclareObjectBaseClass<VBaseUserAction@gamecode>
DeclareObjectBaseClass<VBaseCompartmentSlot@gamecode>
DeclareObjectBaseClass<VBaseEventHandler@gamecode>
DeclareObjectBaseClass<VBaseLightSlot@gamecode>
DeclareObjectBaseClass<VBaseWeaponComponent@gamecode>
// ... and many more
```

These define extensible base classes in the gamecode namespace.

### ClassRegistrator Pattern

Classes are registered using the `ClassRegistrator` pattern:

```
GenericComponentClassRegistrator@gamelib
GenericEntityClassRegistrator@gamelib
ScriptComponentClassRegistrator@gamelib
```

## Scripted Class Extension Points

Classes prefixed with "Scripted" allow script-side extension:

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptComponent` | `gamelib` | Scriptable component base |
| `ScriptedGameTriggerEntity` | `gamecode` | Scriptable trigger entity |
| `ScriptedCameraBase` | `gamecode` | Custom camera base |
| `ScriptedWidgetEventHandler` | `enf` | Widget event handling |
| `ScriptedBackendCallback` | `online@gamelib` | Backend callbacks |
| `AITaskScripted` | `ailib` | Custom AI tasks |
| `DecoratorScripted` | `bt` | Custom BT decorators |

## Type Compatibility

### Cast Errors

| Error | Meaning |
|-------|---------|
| `Cannot convert '%s' to '%s' in argument '%s', method '%s'` | Type conversion failed |
| `ScriptArgsCopy: Pointer inherited types are not supported!` | Inheritance limit in args |
| `ScriptCallQueue: argument '%s': Pointer inherited type '%s' is not supported` | Queue callback limitation |

## Summary Statistics

| Category | Count |
|----------|-------|
| Required base class relationships | 12+ documented |
| Sealed class constraints | 3 error patterns |
| Abstract class constraints | 1 error pattern |
| Override rules | 5 error patterns |
| Component types discovered | 100+ |
| Manager classes | 30+ |
| Module namespaces | 8+ |
