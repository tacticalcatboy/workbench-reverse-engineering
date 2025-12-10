# Enforce Script API Reference

Quick reference for common Arma Reforger / Enfusion classes and their methods.

## Statistics

- **Total Classes:** 8,704
- **Enfusion Core:** 824
- **Arma Reforger:** 7,880
- **Component Classes:** 1,260
- **Entity Classes:** 388
- **Widget Classes:** 200
- **SCR_ Prefixed Classes:** 6,292

---

## Core Base Classes

### GenericComponent

Base class for all entity components.

```enforce
class GenericComponent
{
    // Core Methods
    EntityComponentPrefabData GetComponentData(IEntity ent);
    BaseContainer GetComponentSource(IEntity ent);

    // Event Mask
    int GetEventMask();
    int SetEventMask(IEntity owner, int mask);
    int ClearEventMask(IEntity owner, int mask);

    // Component Lookup
    GenericComponent FindComponent(TypeName typeName);
    int FindComponents(TypeName typeName, array<GenericComponent> outComponents);

    // Lifecycle
    void Activate(IEntity owner);
    void Deactivate(IEntity owner);
    bool IsActive();

    // Events (override these)
    void EOnInit(IEntity owner);
    void EOnFrame(IEntity owner, float timeSlice);
    void EOnActivate(IEntity owner);
    void EOnDeactivate(IEntity owner);
}
```

### IEntity

Base class for all entities in the world.

```enforce
class IEntity extends Managed
{
    // Identity
    EntityID GetID();

    // Hierarchy
    IEntity GetParent();
    IEntity GetRootParent();
    IEntity GetChildren();
    IEntity GetSibling();

    // Data
    VObject GetVObject();
    EntityPrefabData GetPrefabData();
    EntityComponentPrefabData FindComponentData(TypeName typeName);
    BaseWorld GetWorld();

    // LOD
    void SetFixedLOD(int lod);

    // Transform
    void GetTransform(vector mat[]);
    void GetWorldTransform(vector mat[]);
    void GetLocalTransform(vector mat[]);
    void ComputeLocalTransform(vector mat[]);

    // Coordinate Conversion
    vector VectorToParent(vector vec);
    vector CoordToParent(vector coord);
    vector VectorToLocal(vector vec);
    vector CoordToLocal(vector coord);

    // Rotation
    vector GetYawPitchRoll();
    void SetYawPitchRoll(vector angles);

    // Component Access
    GenericComponent FindComponent(TypeName typeName);
}
```

### GenericEntity

Most common entity base class.

```enforce
class GenericEntity extends IEntity
{
    // All IEntity methods plus:
    void SetFlags(EntityFlags flags, bool recursively);
    void ClearFlags(EntityFlags flags, bool recursively);
    EntityFlags GetFlags();
    bool IsFlagSet(EntityFlags flag);
}
```

---

## Component Classes

### BaseRplComponent / RplComponent

Replication component for networked entities.

```enforce
class BaseRplComponent extends GenericComponent
{
    // Replication State
    bool IsProxy();
    bool IsOwner();
    bool IsMaster();

    // Authority
    RplIdentity GetRplIdentity();
    void AskForAuthority();
    void GiveAuthority(RplIdentity identity);
}

class RplComponent extends BaseRplComponent
{
    // Additional replication methods
}
```

### CharacterMovementComponent

Character locomotion control.

```enforce
class CharacterMovementComponent extends GenericComponent
{
    // Movement
    void SetMovement(float forward, float right);
    void SetMovementSpeed(float speed);
    float GetCurrentMovementSpeed();

    // Stance
    void SetStance(ECharacterStance stance);
    ECharacterStance GetStance();
}
```

### BaseSoundComponent

Audio playback on entities.

```enforce
class BaseSoundComponent extends GenericComponent
{
    AudioHandle SoundEvent(string eventName);
    AudioHandle SoundEventOffset(string eventName, vector offset);
    void TerminateAll();
}
```

---

## Entity Classes

### CharacterEntity

Player and AI characters.

```enforce
class CharacterEntity extends PawnEntity
{
    // Inheritance: CharacterEntity -> PawnEntity -> GenericEntity -> IEntity -> Managed
}
```

### PawnEntity

Controllable entities.

```enforce
class PawnEntity extends GenericEntity
{
    // Controller
    PlayerController GetPlayerController();
}
```

---

## Widget Classes

### Widget

Base UI element class.

```enforce
class Widget extends ScriptedWidgetEventHandler
{
    // Visibility
    bool IsVisible();
    void SetVisible(bool visible);
    void SetEnabled(bool enabled);
    bool IsEnabled();

    // Hierarchy
    Widget GetParent();
    Widget GetChildren();
    Widget GetSibling();
    Widget FindWidget(string path);
    Widget FindAnyWidget(string name);

    // Size & Position
    void GetScreenSize(float width, float height);
    void GetScreenPos(float x, float y);
    void SetSize(float width, float height);
    void SetPos(float x, float y);

    // Color
    void SetColor(int color);
    void SetOpacity(float opacity);
}
```

### ButtonWidget

Clickable button element.

```enforce
class ButtonWidget extends UIWidget
{
    // Inheritance: ButtonWidget -> UIWidget -> Widget -> ScriptedWidgetEventHandler -> Managed
}
```

### TextWidget

Text display element.

```enforce
class TextWidget extends UIWidget
{
    void SetText(string text);
    string GetText();
    void SetTextFormat(string format, ...);
}
```

---

## Manager Classes

Common singleton-pattern manager classes:

| Manager | Purpose |
|---------|---------|
| `ActionManager` | Input action bindings |
| `InputManager` | Raw input handling |
| `MenuManager` | Menu/UI stack management |
| `ResourceManager` | Asset loading |
| `SoundManagerModule` | Audio system |
| `WeatherManager` | Weather state |
| `WidgetManager` | UI widget management |

---

## Common SCR_ Classes

Arma Reforger scripted classes (6,292 total):

### Game Mode
- `SCR_BaseGameMode`
- `SCR_BaseGameModeComponent`
- `SCR_GameModeHealthSettings`

### Player
- `SCR_PlayerController`
- `SCR_CharacterControllerComponent`
- `SCR_InventoryStorageManagerComponent`

### Editor
- `SCR_EditorManagerEntity`
- `SCR_EditableEntityComponent`
- `SCR_BaseEditorComponent`

### AI
- `SCR_AIGroup`
- `SCR_AIUtilityComponent`
- `SCR_AICombatComponent`

### Weapons
- `SCR_WeaponComponent`
- `SCR_MuzzleComponent`
- `SCR_MagazineComponent`

### Vehicles
- `SCR_VehicleFactionAffiliationComponent`
- `SCR_VehicleDamageManagerComponent`

---

## Event Handler Signatures

Standard EOn* event methods that can be overridden:

```enforce
// Entity events (require SetEventMask)
override void EOnInit(IEntity owner);
override void EOnFrame(IEntity owner, float timeSlice);
override void EOnActivate(IEntity owner);
override void EOnDeactivate(IEntity owner);

// Physics events
override void EOnContact(IEntity owner, IEntity other, Contact contact);
override void EOnPhysicsActive(IEntity owner, bool activeState);

// Editor events
override bool EOnEditorActivateAsync(int attempt);
override bool EOnEditorDeactivateAsync(int attempt);
override SCR_EditableEntityComponent EOnEditorPlace(
    SCR_EditableEntityComponent parent,
    SCR_EditableEntityComponent recipient,
    EEditorPlacingFlags flags,
    bool isQueue,
    int playerID
);

// Camera events
override bool EOnCameraInit();
override void EOnCameraFrame(SCR_ManualCameraParam param);
override void EOnCameraExit();
```

---

## Type Quick Reference

### Primitives
- `int`, `float`, `bool`, `string`, `vector`

### Reference Types
- `ref` - Counted reference
- `autoptr` - Auto-released pointer
- `weak` - Weak reference (doesn't prevent deletion)
- `notnull` - Guaranteed non-null

### Collections
- `array<T>` - Dynamic array
- `set<T>` - Unique value set
- `map<K,V>` - Key-value mapping

### Common Enums
- `EntityFlags`
- `ECharacterStance`
- `RplRcver` (RPC receiver flags)

---

*Data extracted from Arma Reforger Workbench API documentation.*
