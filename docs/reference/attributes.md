# Enforce Script Attributes Reference

Complete documentation of attributes discovered through reverse engineering of Arma Reforger Workbench.

## Attribute Syntax

Attributes use square bracket syntax placed before declarations:

```enforce
[AttributeName]
[AttributeName()]
[AttributeName(value)]
[AttributeName(param1, param2)]
[AttributeName(name = value)]
[AttributeName(positional, named = value)]
```

## Attribute Categories

### Method Attributes

Attributes that mark methods with special behaviors.

#### EventAttribute

**Namespace:** `gamelib`

Marks a method as an event handler for the ScriptInvoker/event system.

```enforce
[EventAttribute]
void OnMyEvent(IEntity entity, float value)
{
    // Handle event
}
```

**Error Messages:**
- `Method '%s.%s' is not marked with the [EventAttribute] attribute.`

**Validation:**
- Method must be marked with this attribute when registered as an event handler
- Method signature must match the expected event signature

#### ReceiverAttribute

**Namespace:** `gamelib`

Marks a method as a receiver for the callback/delegate system.

```enforce
[ReceiverAttribute]
void OnDataReceived(int data)
{
    // Handle received data
}
```

**Error Messages:**
- `Method '%s.%s' is not marked with the [ReceiverAttribute] attribute.`

**Validation:**
- Required when method is used as a callback receiver
- Signature must match the expected prototype

#### RplRpc Attribute

Marks a method as a Remote Procedure Call for network replication.

```enforce
[RplRpc(RplChannel.Reliable, RplRcver.Server)]
void Rpc_DoAction_S(int actionId)
{
    // Server-side RPC handler
}
```

**Error Messages:**
- `RpcError: Could not find the RPC. Are you missing the RplRpc attribute?`
- `RPC '%s.%s' has parameters that cannot be replicated. RPC calls will be discarded.`
- `RPC '%s.%s' specifies default values for some of its parameters. This is not supported for RPCs.`

**Validation Rules:**
- Parameters must be replicable types
- Default parameter values are NOT supported
- Constructor of parameter types must be parameterless
- Cannot be called from static context

**Naming Conventions (Suffix):**
| Suffix | Meaning |
|--------|---------|
| `_S` | Server-only execution |
| `_O` | Owner-only execution |
| `_BC` | Broadcast to clients |
| `_BCNO` | Broadcast, no owner |

### Class/Property Attributes

#### Attribute (Generic Property Attribute)

The base `Attribute` class is used for exposing script variables to the Workbench editor.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `defvalue` | varies | Default value for the property |
| `desc` | string | Description shown in editor |
| `category` | string | Editor category grouping |
| `uiwidget` | UIWidgets.* | Widget type for editing |
| `editorSetMethod` | string | Method to call when value changes |
| `editorGetMethod` | string | Method to call to get current value |
| `params` | string | Additional parameters |

**Example:**
```enforce
class MyComponent
{
    [Attribute("100", UIWidgets.Slider, "Maximum health", category: "Health", params: "0 1000 1")]
    protected float m_fMaxHealth;

    [Attribute("", UIWidgets.ResourceNamePicker, "Model resource", params: "xob")]
    ResourceName m_sModel;
}
```

**UIWidget Types:**
- `UIWidgets.Auto` - Automatic widget selection
- `UIWidgets.Slider` - Numeric slider
- `UIWidgets.EditBox` - Text input
- `UIWidgets.CheckBox` - Boolean checkbox
- `UIWidgets.ComboBox` - Dropdown selection
- `UIWidgets.ResourceNamePicker` - Resource browser
- `UIWidgets.CurveDialog` - Curve editor
- `UIWidgets.GraphDialog` - Graph editor (deprecated, use CurveDialog)

**Error Messages:**
- `Attribute %s doesn't have parameter %s set up. Set it or remove it from 'Variables' category to turn it into a regular Attribute.`
- `Attribute %s not in 'Variables' category. Add it or remove the use of parameters to turn it into a regular Attribute.`
- `Attribute %s has invalid type %s in it's parameters. Change it for a valid one.`
- `If you define '%s' attribute params you should also define '%s' attribute param for '%s.%s' variable`
- `Property "%s" uses the deprecated UIWidgets::GraphDialog instead of UIWidgets::CurveDialog. It will be removed in the future!`

#### editorGetMethod / editorSetMethod Validation

When using `editorGetMethod` or `editorSetMethod` attribute parameters:

**editorSetMethod Requirements:**
- Method must exist in the class
- Method should have exactly 1 parameter
- Parameter type must match the variable type
- Method should return void

**editorGetMethod Requirements:**
- Method must exist in the class
- Method should have no parameters
- Return type must match the variable type

**Error Messages:**
- `'%s' method from '%s' attribute params of '%s.%s' variable doesn't exist`
- `'%s' method from '%s' attribute params of '%s.%s' variable should have only 1 parameter`
- `'%s' method from '%s' attribute params of '%s.%s' variable should not return any value`
- `'%s' method from '%s' attribute params of '%s.%s' variable parameter type ('%s') is not equal to the variable type ('%s')`
- `'%s' method from 'editorGetMethod' attribute params of '%s.%s' variable doesn't exist`
- `'%s' method from 'editorGetMethod' attribute params of '%s.%s' variable return value type ('%s') is not equal to the variable type ('%s')`
- `'%s' method from 'editorGetMethod' attribute params of '%s.%s' variable should not have any parameter`

### Test Attributes

#### Test Attribute

Marks a class or method as a test for the built-in test framework.

```enforce
[Test("TestSuite")]
class MyTest : TestBase
{
    void TestMethod()
    {
        // Test implementation
    }
}
```

**Error Messages:**
- `TestRegistrationError: Class with Test(...) attribute is not derived from TestBase!`
- `TestRegistrationError: Could not locate target test suite!`
- `TestRegistrationError: Function type test has bad return type!`
- `TestRegistrationError: Function type test has parameters!`

**Validation:**
- Test classes must inherit from `TestBase`
- Test methods should have no parameters
- Test methods should return void (or compatible type)

### Workbench Plugin Attributes

#### WorkbenchPluginAttribute

Marks a class as a Workbench plugin.

**Namespace:** `API`

```enforce
[WorkbenchPluginAttribute("My Plugin", category: "Tools")]
class MyWorkbenchPlugin : WorkbenchPlugin
{
    // Plugin implementation
}
```

#### ButtonAttribute

Creates a button in the Workbench UI.

```enforce
[ButtonAttribute("Click Me")]
void OnButtonClicked()
{
    // Handle button click
}
```

#### MenuBindAttribute

Binds a method to a menu item in Workbench.

```enforce
[MenuBindAttribute("Tools/My Action")]
void OnMenuAction()
{
    // Handle menu action
}
```

### Behavior Tree Attributes

#### BTNodeInAttribute / BTNodeOutAttribute

Marks input/output ports on behavior tree nodes.

```enforce
class MyBTNode : BTNode
{
    [BTNodeInAttribute]
    int m_iInput;

    [BTNodeOutAttribute]
    bool m_bOutput;
}
```

### Cinematic Attributes

#### CinematicEventAttribute

Marks a method or class for the cinematic system.

#### CinematicTrackAttribute

Marks a property for cinematic track editing.

### Forest Generator Attributes

Specialized attributes for the forest generation system:

| Attribute | Purpose |
|-----------|---------|
| `ForestGeneratorDistaceAttribute` | Distance calculation for placement |
| `ForestGeneratorCapsuleStartAttribute` | Capsule start point |
| `ForestGeneratorCapsuleEndAttribute` | Capsule end point |
| `ForestGeneratorGroupIndexAttribute` | Group index for clustering |

**Error Messages:**
- `ForestGeneratorDistaceAttribute not set with DistanceType::BOTTOM, some functionality may not work as expected`
- `ForestGeneratorDistaceAttribute with type %d specified for multiple variables, first occurrence used`
- `ForestGeneratorGroupIndexAttribute not set for any member variable, some functionality may not work as expected`
- `Invalid DistanceType value %d passed to ForestGeneratorDistaceAttribute`

## Data Attribute Classes

These are not square-bracket attributes but configuration classes that inherit from attribute base classes:

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `AimingModifierAttributes` | `gamecode` | Aiming behavior modifiers |
| `AttachmentAttributes` | `gamecode` | Attachment configuration |
| `CharacterModifierAttributes` | `gamecode` | Character stat modifiers |
| `CustomAnimationAttributes` | `gamecode` | Custom animation settings |
| `HolsteredItemAttributes` | `gamecode` | Holstered item display |
| `ItemActionAnimAttributes` | `gamecode` | Action animation settings |
| `ItemAnimationAttributes` | `gamecode` | Item animation settings |
| `ItemAttributeCollection` | `gamecode` | Collection of item attributes |
| `ItemMovementSwayAttributes` | `gamecode` | Movement sway settings |
| `ItemOneHandAnimAttributes` | `gamecode` | One-handed animation |
| `ItemPhysicalAttributes` | `gamecode` | Physical properties (mass, size) |
| `PreviewRenderAttributes` | `gamecode` | Preview rendering settings |
| `WeaponAttachmentAttributes` | `gamecode` | Weapon attachment config |

**Base Class:** `BaseItemAttributeData` (gamecode)

## Attribute Placement Rules

### Valid Placements

| Target | Example |
|--------|---------|
| Class | `[Attribute] class MyClass { }` |
| Method | `[RplRpc] void MyMethod() { }` |
| Property/Field | `[Attribute("default")] int m_iValue;` |

### Multiple Attributes

Multiple attributes can be stacked:

```enforce
[Attribute("100", desc: "Max health")]
[RplProp(condition: RplCondition.Custom)]
protected float m_fMaxHealth;
```

## Variables Category

Properties marked with the `[Attribute()]` decorator are shown in the Workbench editor's "Variables" category by default. This allows modders to configure component settings visually.

**Special Handling:**
- Attributes in "Variables" category require proper parameter setup
- Removing parameters converts to "regular" Attribute
- Invalid parameter types cause validation errors

## Script Variable Warnings

Related warnings for script variables (properties):

| Warning | Meaning |
|---------|---------|
| `Script variable '%s.%s': script default value overwrites value from source` | Default in script overrides data |
| `Script variable '%s.%s': static or const member can't be property` | Invalid property declaration |
| `Script variable '%s.%s': using ResourceName picker with string property, use ResourceName type instead` | Type mismatch for resource picker |
| `Script variable '%s.%s': using weak pointer to store object, use 'ref' for strong reference` | Weak reference warning |

## Native Method Restrictions

Methods marked with certain attributes have restrictions:

```enforce
// Native methods cannot be used with EventAttribute/ReceiverAttribute
Method '%s.%s' methods marked as 'native' are not supported.
```

## Replication Attributes

### RplProp Attribute

Marks a property for network replication:

```enforce
[RplProp(onRplName: "OnHealthChanged")]
protected float m_fHealth;

void OnHealthChanged()
{
    // Called when replicated value changes
}
```

**Constraints:**
- Static variables cannot be replicated
- Constructor of the type must be parameterless

**Error Messages:**
- `Variable '%s.%s' is marked as replicated property, but it is also static. Static variable replication is not supported.`
- `Constructor of type '%s' must not have any parameters when used in RPCs or replicated properties.`

## Best Practices

1. **Always inherit TestBase for test classes** - Required by Test attribute
2. **Use RplRpc naming conventions** - Suffix indicates execution context
3. **Match editorGet/SetMethod signatures** - Types must match exactly
4. **Avoid default values in RPC parameters** - Not supported
5. **Use ResourceName type with ResourceNamePicker** - Not string type
6. **Place in "Variables" category** - For proper editor exposure
