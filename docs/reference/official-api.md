# Official API Documentation

Complete Doxygen-generated API documentation shipped with Arma Reforger Tools.

## Location

```
D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\docs\
├── EnfusionScriptAPIPublic\EnfusionScriptAPIPublic\   # 824 classes
└── ArmaReforgerScriptAPIPublic\ArmaReforgerScriptAPIPublic\  # 7,880 classes
```

## Statistics

| API | Classes | Description |
|-----|---------|-------------|
| EnfusionScriptAPIPublic | 824 | Engine-level API (IEntity, Physics, Math, etc.) |
| ArmaReforgerScriptAPIPublic | 7,880 | Game-level API (Components, AI, Weapons, etc.) |
| **Total** | **8,704** | Complete documented API surface |

## Documentation Structure

### Key Files

| File | Purpose |
|------|---------|
| `index.html` | Documentation home page |
| `classes.html` | Alphabetical class list |
| `hierarchy.html` | Class inheritance hierarchy |
| `functions.html` | All functions A-Z |
| `functions_func.html` | Functions by letter |
| `functions_vars.html` | Variables/properties |
| `group_*.html` | Grouped by category |
| `interface*.html` | Individual class documentation |
| `interface*-members.html` | Class member list |

### Category Groups (Enfusion)

- `group__Attributes.html` - Script attributes
- `group__Audio.html` - Audio system
- `group__Character.html` - Character system
- `group__Components.html` - Component system
- `group__Entities.html` - Entity system
- `group__Events.html` - Event system
- `group__Input.html` - Input handling
- `group__Math.html` - Math utilities
- `group__Physics.html` - Physics system
- `group__Replication.html` - Network replication
- `group__Serialization.html` - Serialization
- `group__UI.html` - User interface
- `group__WidgetAPI.html` - Widget system
- `group__WorkbenchAPI.html` - Workbench tools

## HTML Structure

Each `interface*.html` file contains:

```html
<!-- Method signature -->
<tr class="memitem:...">
  <td class="memItemLeft">proto external ReturnType</td>
  <td class="memItemRight">MethodName(ParamType param, ...)</td>
</tr>
<!-- Method description -->
<tr class="memdesc:...">
  <td class="mdescRight">Description text</td>
</tr>
```

### Method Modifiers

| Modifier | Meaning |
|----------|---------|
| `proto` | Native method (implemented in C++) |
| `external` | External linkage |
| `volatile` | Volatile method |
| `sealed` | Cannot be overridden |
| `out` | Output parameter |
| `notnull` | Non-nullable parameter |

## Example: IEntity Interface

From `interfaceIEntity.html`:

```
proto external EntityID GetID()
  - Return unique entity ID

proto external IEntity GetParent()
  - Returns parent of this entity

proto external void GetTransform(out vector mat[])
  - Returns world transformation of Entity

proto external bool SetTransform(vector mat[4])
  - Sets entity world transformation

proto external int AddChild(notnull IEntity child, TNodeId pivot, EAddChildFlags flags)
  - Add Entity to hierarchy
```

## Usage for AI Training

### Extracting Signatures

The HTML can be parsed to extract:
1. Class name from `<title>` or heading
2. Method signatures from `memItemLeft` + `memItemRight`
3. Descriptions from `memdesc` rows
4. Inheritance from image maps in hierarchy diagrams

### Key Classes to Document

**Enfusion (Engine):**
- `IEntity` - Base entity interface
- `GenericEntity` - Generic entity implementation
- `BaseWorld` - World management
- `Physics` - Physics system
- `Math3D`, `vector`, `matrix` - Math utilities
- `Widget`, `ScriptedWidgetEventHandler` - UI system
- `Resource`, `BaseResourceObject` - Resource system

**Arma Reforger (Game):**
- `SCR_*` - Script components (e.g., `SCR_AIWorld`)
- `*Component` - Game components
- `AI*` - AI system classes
- `*ManagerComponent` - Manager components
- `CharacterControllerComponent` - Character control
- `BaseWeaponManagerComponent` - Weapon management

## Comparison: Reverse Engineering vs Official Docs

| Aspect | Binary Strings | Official Docs |
|--------|---------------|---------------|
| Method names | Partial (from errors) | Complete |
| Parameter types | Some (from errors) | Complete |
| Return types | Some (from errors) | Complete |
| Descriptions | None | Full documentation |
| Internal APIs | Yes (private) | No (public only) |
| Error messages | Yes | No |
| RPC signatures | Yes | Some |

**Recommendation:** Use official docs as primary API reference, binary strings for error messages and internal behavior.
