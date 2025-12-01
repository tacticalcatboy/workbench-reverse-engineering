# Runtime Errors

Errors found **only in the game executable**, not Workbench. These represent runtime errors that occur during script execution.

**Source:** `ArmaReforgerSteamDiag.exe` (v1.6.0.76)

---

## Exception/Crash Patterns

| Pattern | Notes |
|---------|-------|
| `SEH exception thrown. Exception code: 0x%llx at 0x%llx` | Windows structured exception |
| `Unhandled exception` | Uncaught exception |
| `Unknown C++ exception thrown.` | C++ exception |
| `Unknown exception` | Generic exception |
| `Virtual Machine Exception` | VM exception |
| `Virtual machine exception` | VM exception (lowercase) |
| `Application crashed! Generated memory dump: %s` | Application crash |
| `Application hangs (force crash) %.0f s` | Application hang |
| `Invalid copy queue fence value (complete = %d, expected %d), GPU crash is likely` | GPU crash warning |
| `Invalid graphical queue fence value (complete = %d, expected %d), GPU crash is likely` | GPU crash warning |
| `Assertion failed` | Generic assertion |
| `Assertion failed, %s, at %s(%d)` | Assertion with location |

## Script Runtime Errors

| Pattern | Notes |
|---------|-------|
| `Script call: Not enough parameters, expected '%d' got '%d' (method '%s')` | Parameter count mismatch |
| `IReplication::BumpMe::Error: Script called BumpMe from a static context!` | BumpMe static context |
| `IReplication::BumpMe::Error: Script called BumpMe from an Item without any replicable state! class=%s` | BumpMe no state |
| `IReplication::BumpMe::Error: Script called BumpMe from item without layout! This likely means that its class is not derived from native Item type that supports replication. class=%s` | BumpMe no layout |
| `Replication::BumpMe::Error: Script provided an instance of a class that could not be converted to an Item instance! class=%s` | BumpMe conversion error |
| `Error in script binding: can't add class/enum '%s' (already existing)!` | Duplicate binding |
| `Error in script binding: class/enum '%s' declaration is missing in script!` | Missing script declaration |
| `ScriptRpcError: Attempting to call a RPC from outside of the instance!` | RPC outside instance |
| `ScriptSerializer CRC error!` | Script serialization CRC |

## Bounds/Overflow Errors

| Pattern | Notes |
|---------|-------|
| `Array bounds exceeded` | Array out of bounds |
| `Index out of bounds.` | Generic index error |
| `Index out of range (%d >= %d)` | Index with details |
| `Index out of range (%d >= %d) '%s'` | Index with variable name |
| `Instance variable index out of range` | Instance variable bounds |
| `SetVariableValue - index out of bounds` | Variable index error |
| `Subscript out of range on variable %s` | Subscript error |
| `Stack overflow` | Stack overflow |
| `Stack underflow` | Stack underflow |
| `Integer overflow` | Integer overflow |
| `Float overflow` | Float overflow |
| `Float underflow` | Float underflow |
| `Division by zero` | Division by zero |
| `Division by constant zero` | Compile-time div/zero |
| `Division by zero in anim expresion` | Animation expression div/zero |
| `Float divide by zero` | Float div/zero |
| `Integer divide by zero` | Integer div/zero |
| `BitBuffer memory overflow.` | Buffer overflow |
| `Out of range` | Generic range error |
| `Prediction out of range: %u;` | Prediction bounds |

## Entity/World Bounds Errors

| Pattern | Notes |
|---------|-------|
| `Entity out of world bounds. Type '%s', Name '%s', Parent '%s', Object '%s' Coords %f %f %f` | Entity bounds |
| `Out of world bounds detected: %s` | World bounds |
| `Trying to read tile outside the bounds` | Tile bounds |

## Replication (Rpl) Runtime Errors

| Pattern | Notes |
|---------|-------|
| `RplConnection::ValidationError isDevBinary value does not match! local=%u remote=%u` | Dev binary mismatch |
| `RplConnection::ValidationError remote executable version does not match! local=%u.%u.%u.%u local_enf=%u local_game=%u remote=%u.%u.%u.%u remote_enf=%u remote_game=%u` | Version mismatch |
| `RplConnection::ValidationError remote rdb checksum does not match! local=0x%llX remote=0x%llX` | RDB checksum mismatch |
| `RplConnection::ValidationError remote script source code checksum does not match! local=0x%llX remote=0x%llX` | Script checksum mismatch |
| `RplCorruptionError: Could not decode snapshot.` | Snapshot decode failure |
| `RplCorruptionError: Could not read payload.` | Payload read failure |
| `RplCorruptionError: Could not read stream header.` | Stream header failure |
| `RplCreationError: Could not decode msg meta. rootNodeId=0x%08X` | Meta decode failure |
| `RplCreationError: Could not find node! nodeId=0x%08X` | Node not found |
| `RplCreationError: Creation data too large to send over network. size=%zub, node=%s` | Data too large |
| `RplCreationError: Creation method missing or failed! item=%s` | Creation method failure |
| `RplCreationError: Initialization data too large to send over the network. Try reducing the size of data written in RplSave. size=%zub, item=%s` | Init data too large |
| `RplCreationError: Number of items mismatch. expected=%u, created=%zu, nodeId=0x%08X, node='%s'` | Item count mismatch |
| `RplCreationError: RplSave not successful! item=%s` | RplSave failure |
| `RplLayoutError: Node creation was not successful! nodeId=0x%08X, cl='%s', sl='%s'` | Node creation failure |
| `RplLayoutError: could not find cpp layout. nodeId=0x%08X, typeId=0x%016llX` | Missing C++ layout |
| `RplLayoutError: could not find script layout. nodeId=0x%08X, classHash=0x%08X` | Missing script layout |
| `RplLayoutError: layout is missing RplLoadNode method! nodeId=0x%08X, cl='%s' sl='%s'` | Missing RplLoadNode |
| `RplLoadError: Could not find item record for an item in node streaming in. rootNodeId=0x%08X, nodeId=0x%08X, parentNodeId=0x%08X, itemId=0x%08X` | Item record not found |
| `RplLoadError: Could not initialize item. itemId=0x%08X, itemType='%s'` | Item init failure |
| `RplLoadError: Invalid ID on node %s` | Invalid node ID |
| `RplLoadError: Item record has null pointer to item. Item may have been deleted by other item in the hierarchy currently streaming in. rootNodeId=0x%08X, nodeId=0x%08X, parentNodeId=0x%08X, itemId=0x%08X, layout='%s'` | Null item pointer |
| `RplNodeError: Attempting to create a cycle within the node hierarchy!` | Hierarchy cycle |
| `RplNodeError: Attempting to put into hierarchy items where one is already registered into replication and the other is not!` | Hierarchy registration mismatch |
| `RplSchedulerError: Generated task provided id of removed or never registered item! id=0x%08X` | Task item error |
| `RplSoftResyncError: Stream could not be found! item=0x%08X identity=0x%08X` | Stream not found |

## JIP (Join-In-Progress) Errors

| Pattern | Notes |
|---------|-------|
| `IReplication::JIPError: Could not decode cmd msg.` | JIP command decode |
| `IReplication::JIPError: Could not decode cmd response msg.` | JIP response decode |
| `IReplication::JIPError: Could not locate desynced id. (item=0x%08X con=0x%X)` | JIP desync |
| `IReplication::JIPError: Inconsistent item table on Slave connection. Item is missing or different item was loaded in its place.` | JIP item table inconsistency |
| `IReplication::JIPError: Inconsistent item table on Slave connection. Item is missing or different item was loaded in its place. (item=0x%08X layout=%s con=0x%X)` | JIP with full details |
| `IReplication::JIPError: Terminating connection. (identity=0x%08X)` | JIP termination |
| `IReplication::JIPError: Wrong state when starting validation. Terminating connection. state=%u, identity=0x%08X` | JIP validation state error |

## RPC Errors

| Pattern | Notes |
|---------|-------|
| `RpcError: CRpc could not be found by its name hash! itemId=0x%08X item=%s` | RPC not found by hash |
| `RpcError: Calling a RPC from an unregistered item! itemType='%s', rpc='%s'` | RPC from unregistered item |
| `RpcError: Calling a RPC from an unregistred item %s` | RPC unregistered (typo variant) |
| `RpcError: Could not find the RPC. Are you missing the RplRpc attribute?` | Missing RplRpc attribute |
| `ItemReplicatorError: Custom extraction failed rpc=%s, paramIdx=%u` | RPC extraction failure |
| `RPC `%s.%s` has parameters that cannot be replicated. RPC calls will be discarded. See previous errors for details.` | Non-replicable params |
| `FrameCorruption: Could not custom inject RPC param` | RPC param injection |
| `FrameCorruption: Could not decode RPC param! rpc=%s param=%s` | RPC param decode |
| `FrameCorruption: Could not read a RPC! itemId=0x%08X, rpcIdx=%u` | RPC read failure |

## Navmesh/Pathfinding Errors

| Pattern | Notes |
|---------|-------|
| `Failed to initialize Navmesh - Missing project params or invalid navmesh project configuration!` | Navmesh config error |
| `Failed to initialize Navmesh - Not enough memory for navmesh!` | Navmesh memory |
| `Failed to initialize Navmesh - Tile size cannot be less than 1!` | Navmesh tile size |
| `Failed to initialize Navmesh - Too much tiles/polygons in params` | Navmesh overflow |
| `Failed to initialize Navmesh - World parameters are not valid (may be due to missing terrain)!` | Navmesh world params |
| `Failed to initialize Navmesh query - Max query nodes parameter is zero` | Query nodes zero |
| `Failed to initialize Navmesh query - Wrong max query nodes parameter` | Query nodes invalid |
| `Failed to load Navmesh from file! Will initialize empty navmesh world` | Navmesh load failure |
| `Navmesh build: Could not build Detour navmesh.` | Detour build failure |
| `Navmesh build: Could not build distance field.` | Distance field failure |
| `Navmesh build: Could not create compact heightfield.` | Heightfield failure |
| `Navmesh build: Could not create contours.` | Contour failure |
| `Navmesh build: Could not erode.` | Erosion failure |
| `Navmesh build: Out of memory 'rcCompactHeightfield'` | Heightfield OOM |
| `Navmesh build: Out of memory 'rcPolyMesh'.` | PolyMesh OOM |
| `Null path on FindPathOnNavmesh` | Null path |
| `During pathfinding job path was null, which shouldn't happen. Please report.` | Pathfinding null path |
| `Pathfinding: AIBaseMovement - Failed to calculate a path from (%f, %f, %f) to (%f, %f, %f).` | Path calculation failure |
| `Unable to calculate path, fail to find ending navmesh polygon!` | End polygon not found |
| `Unable to calculate path, fail to find starting navmesh polygon!` | Start polygon not found |
| `Unable to calculate path, not enough path nodes in query for findPath!` | Not enough nodes |
| `Unable to calculate path, wrong params in findPath!` | Wrong params |

## Animation Runtime Errors

| Pattern | Notes |
|---------|-------|
| `Animation graph %s contains errors:` | Graph errors |
| `Animation graph is invalid.` | Invalid graph |
| `Animation instance does not match the template of animation graph.` | Instance/template mismatch |
| `%s: anim controller - starting node %s in graph %s doesn't exist` | Starting node missing |
| `%s: anim controller graph %s doesn't exist` | Graph doesn't exist |
| `%s: anim controller graph %s is not valid` | Graph invalid |
| `%s: anim controller initialization data is invalid (graph %s, node %s, instance %s)` | Anim init data invalid |
| `Bone couldn't be found in the skeleton!` | Bone not found |
| `Bone is not present. Bone "%s" on %s, %s` | Bone missing |
| `Bone mask '%s' contains no bones. It will behave as if no mask will be used.` | Empty bone mask |
| `Blending out too many transitions in animation node %s!` | Too many transitions |
| `IK chain bone couldn't be found in the skeleton!` | IK bone missing |

## Graphics/PSO Cache Errors

| Pattern | Notes |
|---------|-------|
| `Cannot create PSO directory %s` | PSO directory creation |
| `Cannot load pso cache %s` | PSO cache load |
| `Cannot rename pso temp cache %s to %s` | PSO cache rename |
| `Invalid file name, pso cache not saved` | Invalid PSO filename |
| `Driver version, cache or adapter mismatch in PSO, trying to create from scratch...` | PSO mismatch |

## Terrain Loading Errors

| Pattern | Notes |
|---------|-------|
| `Terrain '%s' fatal error - terrain materials were not successfully loaded...` | Material load failure |
| `Terrain '%s' fatal error - texture sizes not found in its main data file.` | Old data file |
| `Terrain '%s' tile:%dx%d error - layers was not successfully loaded...` | Layer load failure |
| `Terrain '%s' tile:%dx%d error - grass clutter data was not successfully loaded...` | Grass data failure |
| `Terrain '%s' tile:%dx%d error - holes description was not successfully loaded...` | Hole data failure |
| `Terrain '%s' tile:%dx%d error - disabled blocks description was not successfully loaded...` | Disabled blocks failure |
| `Terrain '%s' tile:%dx%d error - quad materials description was not successfully loaded...` | Quad materials failure |

## Memory/Texture Errors

| Pattern | Notes |
|---------|-------|
| `%s(%d) Out of memory when requested %zd Type: %s %s %s` | Out of memory |
| `Failed to decompress memory image data. Data is not DXT.` | Wrong texture format |
| `Failed to decompress memory image data. Incorrect size (%dx%d) of texture` | Size mismatch |
| `Failed to decompress memory image data. Unsupported source format (%d) of texture` | Unsupported format |
| `Failed to reallocate buffer %S` | Buffer reallocation |
| `VRAM defragmentation end failed` | VRAM defrag failure |
| `Direct3D could not allocate sufficient memory to complete the call.` | D3D memory |

## Network/cURL Errors

| Pattern | Notes |
|---------|-------|
| `error curl_easy_perform, code: %i` | HTTP request failure |
| `error curl_easy_init` | cURL init failure |
| `error curl_multi_init` | Multi-handle init |
| `error creating session: CURLcode = %x` | Session creation |
| `error response body larger than: %u` | Response too large |
| `error headers length over: %u` | Headers too long |
| `error setting up cUrl request, code: %i` | Request setup |
| `Net error: 0x%08X(%d) %s` | Generic network error |
| `QUIC connection error` | QUIC error |
| `QUIC error code: 0x%llx%s%s%s, reason: "%s"` | QUIC detailed error |

## Serialization Errors

| Pattern | Notes |
|---------|-------|
| `Cannot deserialize variable '%s' in class '%s'` | Variable deserialization |
| `Couldn't deserialize string from snapshot.` | String deserialization |
| `Couldn't write string data to packet.` | Packet string write |
| `Couldn't write string data to snapshot.` | Snapshot string write |
| `Couldn't read string length from packet.` | Packet string read |
| `Couldn't read string length from snapshot.` | Snapshot string read |
| `%s class needs to have a constructor with zero arguments when a class is being instantiated by serialization` | Serialization constructor |

## Resource Loading Errors

| Pattern | Notes |
|---------|-------|
| `Resource "%s" read failed` | Resource read failure |
| `ResourceId: Verification failed.` | Resource verification |
| `Couldn't find script declaration for enum %s` | Missing enum declaration |
| `CreateMaterial function failed, material class %s not found` | Material class missing |
| `Couldn't resolve resource name '%s' to an exact or absolute path.` | Resource path resolution |
| `LoadNode failed. Entity streaming-in could not be spawned. prefab='%s' prefabGUID=%016llX prefabEntityId=%016llX nodeId=0x%08X` | Entity spawn failure |
| `LoadNode failed: Entity streaming-in was created without RplComponent. prefab='%s' prefabGUID=%016llX prefabEntityId=%016llX nodeId=0x%08X` | Missing RplComponent |
| `LoadNode failed: No ResourceGUID transfered for nodeId=0x%08X. Can't spawn the prefab!` | No ResourceGUID |
| `Loading of %s failed` | Generic load failure |

## Widget/UI Errors

| Pattern | Notes |
|---------|-------|
| `RichTextWidget '%s': Alignment error` | Rich text alignment |
| `EditBoxWidget '%s': Invalid horizontal text alignment value %d` | Horizontal alignment |
| `EditBoxWidget '%s': Invalid vertical text alignment value %d` | Vertical alignment |

## Unexpected/Unhandled Errors

| Pattern | Notes |
|---------|-------|
| `Unexpected '%s'` | Unexpected token |
| `Unexpected bone direction.` | Bone direction |
| `Unexpected collider type.` | Collider type |
| `Unexpected constraint type.` | Constraint type |
| `Unexpected end of file` | Premature EOF |
| `Unexpected end of line` | Premature EOL |
| `Unexpected end of scope` | Scope error |
| `Unexpected operator '%.*s' (character %d)` | Unexpected operator |
| `Unexpected result state from scripted node: %s` | Script node state |
| `Unexpected simulation type.` | Simulation type |
| `Encountered unhandled error.` | Generic unhandled |

## Connection/Disconnect Errors

| Pattern | Notes |
|---------|-------|
| `Connection disconnected` | Connection lost |
| `Connection failed for group object %s!!!` | Group connection failure |
| `Disconnecting identity=0x%08X: group=%u reason=%u` | Disconnect with reason |
| `Too old connection (%lld seconds idle), disconnect it` | Idle timeout |
| `Too old connection (%lld seconds since creation), disconnect it` | Age timeout |
| `Dropping an unexpected connection request! connectionID=%u` | Unexpected connection |

## Math/Random Errors

| Pattern | Notes |
|---------|-------|
| `Math.RandomFloat: invalid parameters min = %f max = %f` | RandomFloat params |
| `Math.RandomFloatInclusive: invalid parameters min = %f max = %f` | RandomFloatInclusive params |
| `Math.RandomInt: invalid parameters min = %d max = %d` | RandomInt params |
| `Math.RandomIntInclusive: invalid parameters min = %d max = %d` | RandomIntInclusive params |
| `RandomGenerator.RandInt: invalid parameters min = %d max = %d` | RandInt params |
| `RandomGenerator.RandIntInclusive: invalid parameters min = %d max = %d` | RandIntInclusive params |

## Audio/Voice Errors

| Pattern | Notes |
|---------|-------|
| `Voice(%d) not found !!!` | Voice not found |
| `Cannot add effect, effect %zx already present in voice(%d) effects list.` | Duplicate effect |

## Runtime/VM Errors

| Pattern | Notes |
|---------|-------|
| `VM Recursion > 256. Infinite loop?` | Recursion limit |
| `Infinite recursion when loading %s` | Loading recursion |
| `Infinite loop` | Loop detection |
| `Internal compiler error %s : %d` | Internal compiler error |
| `Linker error: Function '%s' is not linked` | Function not linked |
| `Linker error: Function '%s::%s' is not linked` | Method not linked |

## Missing/Not Found Errors

| Pattern | Notes |
|---------|-------|
| `%s is missing %s implementation.` | Missing implementation |
| `%s is missing RplComponent` | Missing RplComponent |
| `%s is missing component %s as required by component %s` | Missing required component |
| `%s rplID=0x%.8X not found` | RplID not found |
| `Class '%s' not found` | Class not found |
| `Cannot find function '%s'` | Function not found |
| `Cannot find bone '%s'` | Bone not found |
| `%s: Child item "%d" not found for @"%s|%s,%d"` | Child item not found |
| `%s: Parent item "%d" not found for @"%s|%s,%d"` | Parent item not found |

## Debug/Diagnostic Messages

| Pattern | Notes |
|---------|-------|
| `%s-DIAG: Error detected in %s (%s)` | Diagnostic error |
| `%d dependencies had error: "%s"` | Dependency error |
| `%s Error UID: "%s" Error Message : "%s"` | Error with UID |
| `Runtime Errors:` | Runtime error list header |
