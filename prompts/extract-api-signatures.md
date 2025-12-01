I'm continuing a Workbench reverse-engineering project to discover API method signatures from Arma Reforger's Enforce Script compiler.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/index.md - Project overview
2. docs/findings/api.md - Current API surface findings (1,833 ClassRegistrator entries)
3. docs/reference/compiler.md - Compiler infrastructure

**Current Task: Extract more API method signatures**

**Data sources:**
- data/workbench/workbench_all_strings.txt (84,718 strings - primary)
- data/game/game_all_strings.txt (61,575 strings - may have runtime API info)

**What's been found so far:**
- 1,833 ClassRegistrator entries (class names exposed to script)
- Key namespaces: enf, gamelib, gamecode, ailib, API, ast
- Some method patterns: FindComponent, GetComponent, AddComponent, GetOwner
- Event system: ScriptInvoker, ScriptCallback, EventHandler

**What needs extraction:**
1. Method signatures from error messages (e.g., "method '%s.%s' has wrong return type")
2. Common method names that appear across classes
3. Property getter/setter patterns (Get%s, Set%s, Is%s, Has%s)
4. Static vs instance method indicators
5. Constructor patterns and requirements
6. Callback/delegate method signatures
7. RPC method patterns (Rpc_ prefixes, RplRpc attribute)
8. Event handler method signatures (EOnInit, EOnFrame, OnXxx)
9. Native vs script method distinctions

**Search strategies to try:**
- `method '%s`, `function '%s`, `Method '`, `Function '` - signature errors
- `Get`, `Set`, `Find`, `Create`, `Add`, `Remove` - method prefixes
- `@` namespace patterns - class::method references
- `Registrator` - registered classes/methods
- `native` - native method bindings
- `argument '%s'`, `parameter` - parameter info
- `return type`, `returns` - return type info
- `static`, `override`, `sealed` - method modifiers

**Goal:** Build a complete picture of the API surface - methods, signatures, parameters, return types. This helps AI understand what's available when writing Enforce Script.

**Output:** Update docs/findings/api.md organized by:
- Namespace/class groupings
- Method categories (lifecycle, getters/setters, events, RPC, etc.)
- Parameter and return type information where available

**When complete:** Move "Extract more API method signatures" to Completed section in docs/getting-started/checklist.md
