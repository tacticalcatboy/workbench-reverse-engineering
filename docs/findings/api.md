# API Surface

Classes and methods exposed to Enforce Script.

## Statistics

| Category | Count |
|----------|-------|
| ClassRegistrator entries | 1,833 |
| RPC methods discovered | 373 |
| EOn* event handlers | 30 |
| Widget event handlers | 30+ |
| Component classes | 100+ |
| Attribute types | 20+ |
| AI Task classes | 40+ |
| Scripted class patterns | 50+ |

## Namespaces

| Namespace | Purpose |
|-----------|---------|
| `enf` | Engine core |
| `gamelib` | Game library |
| `gamecode` | Game-specific code |
| `ailib` | AI library |
| `API` | Public API |
| `ast` | Abstract syntax tree |
| `pov@pathfinding` | Pathfinding/navigation |
| `vhc@gamecode` | Vehicle systems |
| `nm` | Navmesh |
| `online@gamelib` | Online/backend services |
| `bt` | Behavior tree |
| `snd@gamelib` | Sound system |
| `dsp@audio@enf` | Audio DSP effects |
| `il@enf` | Internal/low-level |

## Method Signature Patterns

### Error Messages Revealing Signatures

| Error Pattern | Information Revealed |
|---------------|---------------------|
| `method '%s.%s' has wrong return type` | Class.method format, return type validation |
| `CallFunctionParams: Cannot convert '%s' to '%s' in argument '%s', method '%s'` | Parameter type conversion |
| `Maximum arguments count %d exceeded in method '%s'` | Argument limits |
| `Named arguments on overloaded method '%s' are not supported` | Named argument constraints |
| `Overloaded method '%s', argument name '%s' differs from prototype '%s'` | Overload signature requirements |
| `Not enough parameters in function '%s'` | Required parameter counts |
| `Parameter out/inout '%s' of function '%s' can't accept computed value` | out/inout parameter constraints |
| `Script call: Not enough parameters, expected '%d' got '%d' (method '%s')` | Expected vs actual parameter count |
| `ScriptArgsCopy: Incompatible parameter '%d', expected '%s', got '%s' (method '%s')` | Parameter type mismatch details |
| `EventHandler: Function '%s' called with a wrong type for arg %d. Expecting %s, got %s.` | Event handler signature validation |
| `EventProvider::ThrowEvent: Incompatible parameter '%d', expected '%s', got '%s' (method '%s')` | Event parameter validation |
| `Missing declaration of function '%s' in class '%s'` | Missing method declarations |
| `Multiple declaration of function '%s'` | Duplicate method detection |
| `Method '%s' argument '%s' is not compatible` | Argument compatibility check |
| `Method '%s' is not compatible with prototype '%s', not enough arguments` | Prototype argument count |
| `Method '%s' is not compatible with prototype '%s', too many arguments` | Prototype argument count |
| `Method '%s' is private` | Access modifier validation |
| `Method '%s' is protected` | Access modifier validation |

### Return Type Constraints

| Pattern | Meaning |
|---------|---------|
| `Method '%s.%s' has wrong return type. Expected '%s', found '%s'` | Return type validation |
| `RPC '%s.%s' returns '%s' but only '%s' is allowed` | RPC return restrictions |
| `Wrong usage of '%s' in method '%s.%s': the method return type must be void` | Void return requirements |
| `Custom condition method '%s.%s' has wrong return type` | Condition method constraints |

### Parameter Modifiers

- `out` - Output parameter, cannot accept computed values
- `inout` - Input/output parameter, same constraints as `out`
- Named arguments supported but not on overloaded methods

## Event Handler Methods (EOn*)

Engine-level event callbacks for components and entities.

**Confirmed signature pattern:** `void EOnFrame(class enf::Entity*, float)`

### Lifecycle Events

| Event | Signature | Purpose |
|-------|-----------|---------|
| `EOnInit` | `void EOnInit(IEntity owner)` | Entity initialization |
| `EOnActivate` | `void EOnActivate(IEntity owner)` | Entity activation |
| `EOnDeactivate` | `void EOnDeactivate(IEntity owner)` | Entity deactivation |

### Frame Events

| Event | Signature | Purpose |
|-------|-----------|---------|
| `EOnFrame` | `void EOnFrame(IEntity owner, float timeSlice)` | Per-frame update |
| `EOnFixedFrame` | `void EOnFixedFrame(IEntity owner, float timeSlice)` | Fixed timestep update |
| `EOnPostFrame` | `void EOnPostFrame(IEntity owner, float timeSlice)` | Post-frame processing |
| `EOnPostFixedFrame` | `void EOnPostFixedFrame(IEntity owner, float timeSlice)` | Post fixed-frame |

### Physics Events

| Event | Purpose |
|-------|---------|
| `EOnSimulate` | Physics simulation step |
| `EOnPostSimulate` | Post-simulation processing |
| `EOnPhysicsMove` | Physics movement update |
| `EOnPhysicsActive` | Physics state change |
| `EOnJointBreak` | Physics joint break |
| `EOnTaskSimulate` | Task-based simulation |

### Animation Events

| Event | Purpose |
|-------|---------|
| `EOnAnimEvent` | Animation event callback |
| `EOnDiag` | Diagnostic callback |

### Network Events

| Event | Purpose |
|-------|---------|
| `EOnConnected` | Network connection established |
| `EOnDisconnected` | Network disconnection |
| `EOnPlayerConnected` | Player joined |
| `EOnPlayerDisconnected` | Player left |

### Navmesh/Pathfinding Events

| Event | Purpose |
|-------|---------|
| `EOnGenerateRequest` | Navmesh generation requested |
| `EOnGenerationFinished` | Navmesh generation complete |
| `EOnPathTypeChanged` | Path type changed |
| `EOnEraseTilesRequest` | Tile erase requested |

### Editor Events (Workbench-only)

| Event | Purpose |
|-------|---------|
| `EOnChangePolygonDataAction` | Polygon data changed |
| `EOnPolygonDataCopy` | Polygon data copied |
| `EOnRebuildChangedTilesButtonClicked` | Rebuild tiles button |
| `EOnRebuildTileButtonClicked` | Rebuild tile button |
| `EOnTogglePolygonAction` | Toggle polygon action |
| `EOnVisualizationSelectionChanged` | Visualization changed |
| `EOnYOffsetChanged` | Y offset changed |
| `EOnSetupPathFilterClicked` | Path filter setup |
| `EOnToolButtonClicked` | Tool button clicked |
| `EOnVisualizationTypeChanged` | Visualization type changed |

## RPC Methods (Network Replication)

**Total discovered: 373 RPC methods across 50+ components**

### RPC Naming Conventions

| Suffix | Meaning |
|--------|---------|
| `_S` | Server-only execution |
| `_O` | Owner-only execution |
| `_BC` | Broadcast to clients |
| `_BCNO` | Broadcast, no owner |
| `_BCU` | Broadcast unreliable |
| `_BCR` | Broadcast reliable |
| `_SR` | Server reliable |
| `_SU` | Server unreliable |
| `_BNOR` | Broadcast, no owner reliable |
| `_EntityID` | Entity ID variant |

### RPC Method Examples by Component

#### ActionsPerformerComponent
```
Rpc_CancelAction, Rpc_CancelActionBC
Rpc_PerformAction, Rpc_PerformActionBC, Rpc_PerformActionFirst
Rpc_PerformContinuousAction, Rpc_PerformContinuousActionFirst
Rpc_StartAction, Rpc_StartActionBC
```

#### InventoryStorageManagerComponent
```
Rpc_DeleteItem, Rpc_DeleteItemFailed
Rpc_InsertItem, Rpc_InsertItemFailed
Rpc_MoveItem, Rpc_MoveItemFailed
Rpc_RemoveItem, Rpc_RemoveItemFailed
Rpc_ReplaceItem, Rpc_ReplaceItemFailed
Rpc_RequestDeleteItem, Rpc_RequestInsertItem
Rpc_RequestSpawnItem, Rpc_RequestSwapItems
Rpc_SwapItems, Rpc_SwapItemsFailed
Rpc_VerifyMagazineCount
```

#### CharacterControllerComponent
```
Rpc_AckInputActionFail_O, Rpc_AckInputActionSuccess_O
Rpc_AskInputAction
Rpc_DoSetFireMode_BCNO, Rpc_DoSetMuzzle_BCNO
Rpc_DoSetSafety_BCNO, Rpc_DoSetSightsRange_BCNO
Rpc_RequestExecuteCharacter
Rpc_RequestSetFireMode, Rpc_RequestSetMuzzle
RPC_SetUnconscious_BC, RPC_SetUnconscious_O
RPC_Link_BC, RPC_Link_S, RPC_Unlink_BC, RPC_Unlink_S
```

#### BaseWeaponManagerComponent
```
Rpc_DoFireEmpty_BCNO, Rpc_DoFire_BCNO, Rpc_DoThrow_BCNO
Rpc_RequestFire, Rpc_RequestFireEmpty, Rpc_RequestFireMat
Rpc_RequestThrow_S
Rpc_SetVisibleAllWeapons_BCNO, Rpc_SetVisibleCurrentWeapon_BCNO
Rpc_SetWeaponPassiveMode_BCNO
```

#### PlayerController
```
Rpc_AskSetDate, Rpc_AskSetDayDuration
Rpc_AskSetTimeOfTheDay, Rpc_AskSetTimeAutoAdvance
Rpc_AskSetRainIntensityOverride
Rpc_AskSetWindDirectionOverride, Rpc_AskSetWindSpeedOverride
Rpc_RequestFullGraphSync_S, Rpc_RequestRespawn_S
```

#### DamageManagerComponent
```
Rpc_EnableDamageHandling, Rpc_EnableDamageHandling_BC
RPC_TakeDamage_BC
RPC_SetAndReplicateInstigator_BC
```

#### BaseLightManagerComponent
```
Rpc_SetLightEnabledBC, Rpc_SetLightEnabledS
Rpc_SetLightFunctionalBC, Rpc_SetLightFunctionalS
Rpc_SetLightInhibitedBC, Rpc_SetLightInhibitedS
Rpc_SetLightStateBC, Rpc_SetLightStateS
Rpc_SetLightsStateBC, Rpc_SetLightsStateS
Rpc_SetSurfaceFunctionalBC, Rpc_SetSurfaceFunctionalS
Rpc_SetVisibilityBC, Rpc_SetVisibilityS
```

#### BaseWeatherManagerEntity
```
RPC_SetDateBC, RPC_SetDayDurationBC
RPC_SetTimeOfTheDayBC, RPC_SetIsDayAutoAdvancedBC
RPC_SetRainIntensityOverrideBC, RPC_SetWetnessBC
RPC_SetWindDirectionOverrideBC, RPC_SetWindSpeedOverrideBC
RPC_SetFogAmountOverrideBC, RPC_SetFogHeightDensityOverrideBC
RPC_SetLatitudeBC, RPC_SetLongitudeBC
RPC_SetTimeZoneOffsetBC, RPC_SetDSTEnabledBC
```

#### CharacterCommandHandlerComponent
```
RPC_AttachCharacterToCompartment_BC, RPC_AttachCharacterToCompartment_S
RPC_DetachCharacterFromCompartment_BC, RPC_DetachCharacterFromCompartment_S
RPC_RequestDesyncDetectionUpdate_S, RPC_SendDesyncDetectionUpdate_O
RPC_StartEndVehicleCommand_BC, RPC_StartEndVehicleCommand_S
RPC_SyncItemUseState_BCNO
```

#### NwkMovementComponent
```
Rpc_UpdateTransformStart_BNOR, Rpc_UpdateTransformStart_SR
Rpc_UpdateTransform_Empty_SR, Rpc_UpdateTransform_SR
Rpc_USendMove_S (various movement components)
```

#### HitZoneContainerComponent
```
RPC_HitZone_SetHealth_BC, RPC_HitZone_SetMaxHealth_BC
RPC_HitZone_SyncDamageState_BC, RPC_HitZone_SyncHealth_BC
RPC_ApplyQueuedDamageStates_BC
Rpc_HitZone_SetDamageOverTime_BC
```

#### TurretControllerComponent
```
Rpc_AckInputActionFail_O, Rpc_AckInputAction_BC
Rpc_AddMagazineSyncReference_BC, Rpc_RemoveMagazineSyncReference_BC
Rpc_AskInputAction, Rpc_SetWeaponGroup_BCNO, Rpc_SetWeaponGroup_S
Rpc_UpdateAimLimits_BC, Rpc_UpdateAimLimits_S
Rpc_UpdateFlags_BC, Rpc_UpdateFlags_S
```

#### VehicleControllerComponent
```
Rpc_AckInputActionFail_O, Rpc_AckInputAction_BC
Rpc_AskInputAction
Rpc_LockPilotControls_BC, Rpc_SetCompartmentPiloting_BC
```

#### DialogueSystem
```
RPC_EventCreate_BC, RPC_EventInterrupt_BC
RPC_EventResponse_BC, RPC_EventSkip_BC
RPC_EventStartAt_BC, RPC_EventStart_BC
```

#### RplConnection
```
Rpc_CrashServer, Rpc_FlushServerRplTrace, Rpc_FreezeServer
Rpc_LoadMissionFromResourceId_O, Rpc_LoadWorldFromFilePath_O
Rpc_PrepareReload_O, Rpc_ReadyForReload_S
Rpc_SetServerStatsEnabled
Rpc_ValidationPassed_O, Rpc_Validation_S
Rpc_WorldLoaded_S, Rpc_DisconnectReason_O
```

### RPC Constraints

- Must have `[RplRpc]` attribute
- Return type restrictions apply
- Constructor of parameter types must be parameterless
- Cannot use static context: `IReplication::BumpMe::Error: Script called BumpMe from a static context!`

## Callback/Delegate System

### ScriptInvoker

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptInvoker` | `gamelib` | Event invoker for callbacks |
| `ScriptInvokerBase` | - | Base class |

Errors:
- `ScriptInvoker: Recursive call of Invoke!`
- `ScriptInvoker::Invoke: Incompatible parameter '%d', expected '%s', got '%s' (method '%s')`

### ScriptCallback

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptCallback` | `enf` | Callback handler |
| `ScriptCallbackManager` | `enf` | Manages callbacks |
| `ScriptCallbackBase` | `il@enf` | Internal base |

Constraints:
- `ScriptCallback: method '%s' is private/protected` - Method must be accessible
- `Callback method '%s' has not supported arguments!`
- `Callback method '%s' is not compatible with prototype '%s'`
- `Can't make callback from non-static function '%s' without instance`
- `Can't make callback on type '%s' (must be inherited from Managed)`

### ScriptCallQueue

- `ScriptCallQueue: argument '%s': Pointer inherited type '%s' is not supported`
- `ScriptCallQueue: argument '%s': Static Arrays not supported`

## Static vs Instance Methods

### Detection Patterns

| Error | Meaning |
|-------|---------|
| `Trying to access non-static member '%s' from static method '%s'` | Instance member in static context |
| `Trying to call non-static function '%s' as static` | Instance method called statically |
| `Method '%s' is linked as member but declared as external/static` | Linkage mismatch |
| `Method '%s' is linked as static/external but declared as member` | Linkage mismatch |
| `Function '%s' override signature conflict: differing 'static' usage` | Override static mismatch |

### Static Variable Constraints

- `Variable '%s' is not static`
- `Variable '%s' in pseudo-class '%s' must be static/const`
- `static/const variables can't be auto`
- `Variable '%s.%s' is marked as replicated property, but it is also static. Static variable replication is not supported.`
- `Script variable '%s.%s': static or const member can't be property`

## Constructor Patterns

### Requirements

| Scenario | Requirement |
|----------|-------------|
| Serialization | Zero-argument constructor required |
| RPC parameters | Constructor must have no parameters |
| Widget components | Arg-less constructor required |
| Cloning | Constructor must be public |

### Error Messages

- `%s class needs to have a constructor with zero arguments when using serialization`
- `%s class needs to have a constructor with zero arguments when a class is being instantiated by serialization`
- `Constructor of type '%s' must not have any parameters when used in RPCs or replicated properties`
- `Can't clone class '%s', constructor is not public`
- `Cannot call constructor or destructor '%s' method directly!`
- `Multiple declaration constructor '%s'`
- `WidgetComponent '%s' has no suitable constructor (arg-less) to call`
- `Constructor '%s', argument '%s' is not compatible with prototype argument type or spec '%s'`

## Attributes

### Script Attributes

| Attribute | Namespace | Purpose |
|-----------|-----------|---------|
| `EventAttribute` | `gamelib` | Marks event methods |
| `ReceiverAttribute` | `gamelib` | Marks receiver methods |
| `RplRpc` | - | Marks RPC methods |
| `ButtonAttribute` | - | UI button attribute |

### Attribute Errors

- `Method '%s.%s' is not marked with the [EventAttribute] attribute`
- `Method '%s.%s' is not marked with the [ReceiverAttribute] attribute`
- `Method '%s.%s' methods marked as 'native' are not supported`
- `RpcError: Could not find the RPC. Are you missing the RplRpc attribute?`

### Data Attributes

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `AimingModifierAttributes` | `gamecode` | Aiming modifiers |
| `AttachmentAttributes` | `gamecode` | Attachment config |
| `CharacterModifierAttributes` | `gamecode` | Character modifiers |
| `ItemPhysicalAttributes` | `gamecode` | Item physics |
| `ItemAnimationAttributes` | `gamecode` | Item animation |
| `HolsteredItemAttributes` | `gamecode` | Holstered item config |
| `WeaponAttachmentAttributes` | `gamecode` | Weapon attachments |
| `PreviewRenderAttributes` | `gamecode` | Preview rendering |

## Inheritance & Class System

### Inheritance Constraints

- `'%s': cannot derive from sealed type '%s'`
- `'%s.%s': cannot override inherited member '%s' because it is sealed`
- `'%s.%s': cannot override inherited member '%s' because it is private`
- `Circle inheritance in class '%s'`
- `Can't inherit class '%s'`
- `Sealed type '%s' can't be modded`

### Override Requirements

- `Function '%s' is marked as override, but there is no function with this name in the base class`
- `Overriding function '%s' but not marked as 'override'`
- `Method '%s::%s' already declared in parent class '%s'`

### Class Registration

- `ClassRegistrator@%s` - Individual class registration
- `RegisterScriptClasses` - Bulk registration method
- `ScriptRegistrator` - Script registration system
- `GenerateScriptDeclaration` - Declaration generation

### Type Requirements

- `Component Class '%s' must inherit from '%s'`
- `Entity Class '%s' must inherit from '%s'`
- `Game::SpawnEntity: Class must inherits from GenericEntity!`
- `Script class must be inherited from BaseLoadingAnim`

## Replication System

### Replication Errors

| Error | Meaning |
|-------|---------|
| `Type '%s' cannot be replicated due to previous errors` | Type not replicable |
| `Type '%s' has wrong replication callbacks` | Bad callbacks |
| `RPC '%s.%s' has parameters that cannot be replicated` | Non-replicable params |
| `Attempting to add instance of type '%s' as an item to RplNode, but this type has no replication layout` | Missing layout |

### Replication Callbacks

- `OnRpl callback method '%s.%s' has wrong return type. Expected '%s', found '%s'`
- `ScriptCallback_OnRpl` - Replication callback type
- `ScriptCallback_CustomRpcCondition` - Custom RPC condition

### RplNode System

- `RplCreationError: Creation method missing or failed!`
- `RplLayoutError: layout is missing RplLoadNode method!`
- `RplLoadError: Could not initialize item`
- `IReplication::BumpMe::Error: Script called BumpMe from item without layout!`

## Component System

### Common Component Methods

| Pattern | Purpose |
|---------|---------|
| `FindComponent` | Find component by type |
| `GetComponent` | Get component reference |
| `AddComponent` | Add component dynamically |
| `GetOwner` | Get owning entity |
| `SetOwner` | Set owning entity |
| `GetOwnerEntity` | Get owner as entity |

### Major Component Classes

| Component | Purpose |
|-----------|---------|
| `ActionsPerformerComponent` | Action execution |
| `CharacterControllerComponent` | Character control |
| `CharacterMovementComponent` | Character movement |
| `CharacterAnimationComponent` | Character animation |
| `InventoryStorageManagerComponent` | Inventory management |
| `BaseWeaponManagerComponent` | Weapon management |
| `BaseLightManagerComponent` | Light management |
| `DamageManagerComponent` | Damage handling |
| `FactionAffiliationComponent` | Faction system |
| `HitZoneContainerComponent` | Hit detection |
| `CompartmentAccessComponent` | Vehicle compartments |
| `BaseAnimPhysComponent` | Animation physics |
| `BaseChatComponent` | Chat system |
| `AIBehaviorTreeComponent` | AI behavior |
| `AIPathfindingComponent` | AI navigation |

## Entity System

### Entity Methods

- `Entity::AddChild` - Add child entity
- `Entity::SetLocalTransform` - Set local transform
- `Entity::SetWorldTransform` - Set world transform
- `EntitySlotInfo::SetAttachedEntity` - Attach entity to slot

### Entity Events

- `PlayerController::SetControllerEntity` - Must be called from server
- `BaseWeatherManagerEntity::RPC_SetTimeOfTheDayBC` - Weather time

## Widget System

### Widget Event Types

| Event | Purpose |
|-------|---------|
| `WidgetEventClick` | Click event |
| `WidgetEventFocus` | Focus gained |
| `WidgetEventFocusLost` | Focus lost |
| `WidgetEventChar` | Character input |
| `WidgetEventController` | Controller input |
| `WidgetEventChange` | Value changed |
| `WidgetEventEnable` | Widget enabled |
| `WidgetEventDisable` | Widget disabled |
| `WidgetEventHide` | Widget hidden |
| `WidgetEventChildAdd` | Child added |
| `WidgetEventChildRemove` | Child removed |
| `WidgetEventItemSelected` | Item selection |
| `WidgetEventLinkClick` | Link clicked |
| `WidgetEventCustom` | Custom event |

### Widget Event Handler Methods

| Handler Method | Purpose |
|----------------|---------|
| `OnClick` | Click handler |
| `OnDoubleClick` | Double-click handler |
| `OnChange` | Value change handler |
| `OnFocus` | Focus gained handler |
| `OnFocusLost` | Focus lost handler |
| `OnChar` | Character input handler |
| `OnController` | Controller input handler |
| `OnEnable` | Widget enabled handler |
| `OnDisable` | Widget disabled handler |
| `OnShow` | Widget shown handler |
| `OnHide` | Widget hidden handler |
| `OnChildAdd` | Child added handler |
| `OnChildRemove` | Child removed handler |
| `OnItemSelected` | Item selection handler |
| `OnLinkClick` | Link click handler |
| `OnLinkEnter` | Link hover enter |
| `OnLinkLeave` | Link hover leave |
| `OnMouseEnter` | Mouse enter handler |
| `OnMouseLeave` | Mouse leave handler |
| `OnMouseMove` | Mouse move handler |
| `OnMouseWheel` | Mouse wheel handler |
| `OnMouseButtonDown` | Mouse button press |
| `OnMouseButtonUp` | Mouse button release |
| `OnModalClickOut` | Click outside modal |
| `OnModalClosed` | Modal closed handler |
| `OnCustomEvent` | Custom event handler |
| `OnUpdate` | Update handler |
| `OnWriteModeEnter` | Write mode enter |
| `OnWriteModeLeave` | Write mode leave |

### Widget Handlers

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptedWidgetEventHandler` | `enf` | Script widget handler |
| `WidgetEventHandler` | `enf` | Base widget handler |

## Logging & Diagnostics

### Log Levels (Priority Order)

| Level | Priority |
|-------|----------|
| Fatal | Highest |
| Error | High |
| Warning | Medium |
| Normal | Standard |
| Verbose | Low |
| Debug | Lower |
| Spam | Lowest |

### Diagnostic Classes

| Class | Purpose |
|-------|---------|
| `DiagMenuAPIRegistrator` | Diagnostic menu |
| `DiagMenuWidget` | Menu widget |
| `EDiagMenuGame` | Game menu enum |
| `EDiagMenuGameLib` | GameLib menu enum |
| `LogLevelRegistrator` | Log level registration |

## AI System

### AI Components

| Component | Purpose |
|-----------|---------|
| `AIBehaviorTreeComponent` | Behavior trees |
| `AIPathfindingComponent` | Navigation |
| `AIControlComponent` | AI control |
| `AICombatPropertiesComponent` | Combat behavior |
| `AIKnowledgeComponent` | Knowledge base |
| `AIFormationComponent` | Formation handling |

### AI Tasks

All discovered AI task classes (from ClassRegistrator):

**Movement Tasks:**
- `AITaskMove` - Basic movement
- `AITaskMoveToEntity` - Move to entity
- `AITaskMoveToWaypoint` - Move to waypoint
- `AITaskMoveInFormation` - Formation movement
- `AITaskGroupMove` - Group movement
- `AITaskGroupMoveToEntity` - Group move to entity
- `AITaskStop` - Stop movement
- `AITaskCharacterStop` - Character stop
- `AITaskOrient` - Orientation

**Combat Tasks:**
- `AITaskAim` - Basic aiming
- `AITaskCharacterAim` - Character aiming
- `AITaskFire` - Fire weapon
- `AITaskReload` - Reload weapon
- `AITaskThrowGrenade` - Throw grenade
- `AITaskCharacterRaiseWeapon` - Raise weapon
- `AITaskPickTarget` - Target selection

**Vehicle Tasks:**
- `AITaskGetInVehicle` - Enter vehicle
- `AITaskGetOutVehicle` - Exit vehicle

**Action Tasks:**
- `AITaskPerformSmartAction` - Smart action
- `AITaskPerformObjectAction` - Object action
- `AITaskRequestAction` - Request action
- `AITaskPlayGesture` - Play gesture

**Control Tasks:**
- `AITaskCreateGroup` - Create AI group
- `AITaskSendOrder` - Send order
- `AITaskFinishOrder` - Finish order
- `AITaskCurrentOrder` - Current order
- `AITaskCallMethod` - Call method
- `AITaskScripted` - Scripted task

**State Tasks:**
- `AITaskChangeStance` - Change stance
- `AITaskSetADS` - Set ADS
- `AITaskSetMovementSpeed` - Set speed
- `AITaskCharacterSetMovementSpeed` - Character speed
- `AITaskGroupSetMovementSpeed` - Group speed
- `AITaskSetVariable` - Set variable
- `AITaskReturnState` - Return state
- `AITaskIdle` - Idle state
- `AITaskClearDanger` - Clear danger

**Query Tasks:**
- `AITaskFindEntity` - Find entity
- `AITaskFindSmartAction` - Find smart action
- `AITaskGetAimingPosition` - Get aim position
- `AITaskGetControlledEntity` - Get controlled entity
- `AITaskGetCurrentSmartAction` - Get current smart action
- `AITaskGetFormationOffset` - Get formation offset
- `AITaskGetGroupChildren` - Get group children
- `AITaskGetSmartActionParams` - Get action params
- `AITaskGetWaypoint` - Get waypoint
- `AITaskCreatePosition` - Create position

**Pathfinding Tasks:**
- `AITaskSetPathfindingFilters` - Set path filters
- `AITaskResetPathfindingFilters` - Reset path filters

## Validation System

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `EntityValidationBase` | `enf` | Base validation |
| `EntityValidationCollection` | `enf` | Validation collection |
| `EntityDataValidation` | `gamelib` | Entity validation |
| `EntitySkewValidation` | `gamelib` | Skew validation |
| `WorldBoundsValidation` | `gamelib` | Bounds validation |
| `WaterBodyValidation` | `gamelib` | Water validation |
| `ValidateScripts` | `NetApiNative` | Script validation |
| `EScriptValidationResult` | - | Result enum |

## Threading

- `Cannot create thread out of non-script function '%s'` - Thread creation constraint
- Thread creation only from script functions

## Game System Methods

### Core Game Methods

```
Game::LoadEntities - Load entities
Game::SpawnEntity - Spawn entity (must inherit from GenericEntity)
Game::SpawnEntityPrefab - Spawn from prefab template
```

### ChimeraGame Events

```
ChimeraGame::OnChimeraWorldBeforeEntitiesCreated()
ChimeraGame::OnChimeraWorldBeforeEntitiesInitialized()
ChimeraGame::OnChimeraWorldEntitiesInitialized()
```

## Scripted Classes

Common "Scripted" class patterns that allow script-side extension:

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptedCameraBase` | `gamecode` | Custom camera base |
| `ScriptedCameraItem` | `gamecode` | Camera item |
| `ScriptedCameraSet` | `gamecode` | Camera set |
| `ScriptedWidgetEventHandler` | `enf` | Widget handler |
| `ScriptedBackendCallback` | `online@gamelib` | Backend callback |
| `ScriptedBaseZeroingGenerator` | `gamecode` | Zeroing generation |
| `ScriptedBaseSndModule` | `snd@gamelib` | Sound module |
| `AITaskScripted` | `ailib` | Scripted AI task |
| `DecoratorScripted` | `bt` | Scripted decorator |
| `DecoratorTestScripted` | `ailib` | AI test decorator |
| `AnimPhysCommandScripted` | `gamelib` | Animation command |
| `CharacterCommandScripted` | `gamecode` | Character command |
| `ScriptedAABGridMap` | `gamecode` | Grid map |
| `ScriptedCircleGridMap` | `gamecode` | Circle grid map |
| `ScriptedGraphNode` | `gamecode` | Graph node |
| `ScriptedGraphEdge` | `gamecode` | Graph edge |

## Physics System

### Physics Creation Methods

```
Physics::CreateDynamic - Create dynamic body (requires world)
Physics::CreateDynamicEx - Extended dynamic creation
Physics::CreateGhostEx - Create ghost body
Physics::CreateStatic - Create static body
Physics::CreateStaticEx - Extended static creation
```

### Physics Errors

- Creating body on entity with no world fails
- Must have valid world context for physics operations

## Unknown / Needs Research

- Complete method signatures for all registered classes
- Full parameter types for each method
- Property getter/setter implementation details (Get%s/Set%s patterns)
- Complete list of valid attribute parameters
- Full preprocessor directive support
- Exact Physics:: method signatures
- Audio DSP effect parameter structures
