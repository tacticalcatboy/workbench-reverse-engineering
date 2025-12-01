# Script Module System

The Enforce Script module system manages script code organization, compilation, and cross-module visibility in Arma Reforger.

## Module Names and Purposes

### Core Script Modules

| Module | Project File | Purpose |
|--------|-------------|---------|
| Engine | `scripts/projects/Engine.sproj` | Core engine scripting (lowest level) |
| Entities | `scripts/projects/Entities.sproj` | Entity system scripts |
| GameLib | `scripts/projects/GameLib.sproj` | Game library - shared gameplay code |
| Game | `scripts/projects/Game.sproj` | Game-specific code |
| Workbench | `scripts/projects/Workbench.sproj` | Workbench editor tools (editor only) |
| WorkbenchGame | `scripts/projects/WorkbenchGame.sproj` | Workbench game integration (editor only) |

### Module Internal Names

From string extraction:
- `ModuleEntities` - Entities module
- `ModuleGameLib` - GameLib module
- `ModuleWorkbenchGame` - Workbench game module

### Script Directory Paths

Resource references with GUIDs:
- `{53AB5D17A4D25BC6}scripts/GameLib`
- `{B92491157EA3E4AD}scripts/Game`

## Module Hierarchy and Dependencies

### Compilation Order

Based on compilation messages, modules compile in dependency order:
1. Engine (lowest level)
2. Entities
3. GameLib (message: `Compiling GameLib scripts`)
4. Game (message: `Compiling Game scripts`)
5. WorkbenchGame (editor only)

### Inferred Dependency Chain

```
Engine
  └── Entities
       └── GameLib
            └── Game
                 └── WorkbenchGame (editor only)
```

### Cross-Module Type Restrictions

Error message: `Type '%s' is declared in different script module`

This indicates the compiler enforces module boundaries for type declarations. Classes cannot be redeclared across modules.

## Module Classes (C++ Infrastructure)

### Core Classes

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptModule` | `enf` | Main module class |
| `ScriptModuleRef` | `API@enf` | Module reference (API exposure) |
| `ScriptModulePathClass` | `enf` | Module path handling |
| `ScriptContext` | `enf` | Script execution context |
| `EnforceScriptContext` | `enf` | Enhanced script context |
| `ScriptCompilerContext` | (struct) | Compilation context |

### Script Project Management

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptProject` | `enf` | Base project class |
| `ScriptProjectManager` | `enf` | Manages all script projects |
| `ScriptProjectManagerGame` | `gamelib` | Game-specific project manager |
| `ScriptProjectFile` | `enf` | Individual script file |
| `ScriptProjectItem` | `enf` | Project item |
| `ScriptProjectTree` | - | Project structure (Workbench) |

### Module-Specific Project Classes

| Class | Namespace | Purpose |
|-------|-----------|---------|
| `ScriptProjectEngine` | `gamelib` | Engine scripts project |
| `ScriptProjectEntities` | `gamelib` | Entities scripts project |
| `ScriptProjectGameLib` | `gamelib` | GameLib scripts project |
| `ScriptProjectGame` | `gamelib` | Game scripts project |
| `ScriptProjectWorkbench` | - | Workbench scripts (editor) |
| `ScriptProjectWorkbenchGame` | - | WorkbenchGame scripts (editor) |

## Compilation and Loading Process

### Compilation Messages

| Message | Meaning |
|---------|---------|
| `Compiling GameLib scripts` | GameLib module compilation started |
| `Compiling Game scripts` | Game module compilation started |
| `Can't compile "%s" script module!` | Module compilation failed |
| `Compilation failed for @"%s"` | Specific file compilation failed |
| `Addon cannot be packed due to failed script compilation!` | Pack blocked by errors |
| `Initializing scripts` | Script system initialization |
| `ScriptProjectManager init` | Project manager initializing |

### Loading Infrastructure

| Class/Method | Purpose |
|--------------|---------|
| `ScriptModule::LoadScript` | Load script into module |
| `LoadScriptJob` | Async script loading job |
| `EnforceScriptContext::LoadScript` | Context-based loading |
| `EnforceScriptContext::CompileModule` | Module compilation |
| `ReloadScriptsEvent` | Script reload event |

### Compilation Lifecycle Events

Workbench compilation hooks:
- `BeforeWorkbenchScriptsCompile` - Before WB scripts compile
- `AfterWorkbenchScriptsCompile` - After WB scripts compile
- `AfterWorkbenchGameScriptsCompile` - After WB game scripts compile
- `OnWBScriptsRecompile` - WB scripts recompiled
- `ScriptsCompiled` - Scripts compilation complete

## Cross-Module Class Visibility

### Type Resolution Errors

| Error | Meaning |
|-------|---------|
| `Type '%s' is declared in different script module` | Type belongs to another module |
| `Class '%s' not found` | Class not in scope |
| `Unknown class '%s'` | Class doesn't exist |
| `Missing script declaration for c++ class '%s'` | C++ class missing script binding |
| `Missing script declaration of class '%s'` | Class declaration missing |

### Class Inheritance Constraints

Classes in lower modules cannot reference classes in higher modules:
- GameLib classes **cannot** depend on Game classes
- Engine classes **cannot** depend on GameLib classes

Module-specific class requirements:
- `Script class handling initial splash screen. Must be inherited from BaseLoadingAnim and be in GameLib script module.`

### Sealed Types

- `'%s': cannot derive from sealed type '%s'`
- `Sealed type '%s' can't be modded`

Sealed classes cannot be inherited from in other modules or mods.

## Module Lifecycle Methods

### Module Initialization

| Error/Message | Meaning |
|---------------|---------|
| `module initialization error` | Module failed to initialize |
| `Can't initialize script callbacks module` | Callback module init failed |
| `Can't load init script: %s` | Init script load failed |
| `noGameScriptsOnInit` | Game scripts disabled on init |

### ScriptModule Methods

| Method | Purpose |
|--------|---------|
| `ScriptModule.Call` | Call method in module |
| `ScriptModule::LoadScript` | Load script file |
| `ScriptModule->New()` | Create new instance |

Access control error: `ScriptModule.Call: method '%s' is private/protected`

### Module Retrieval

| Method | Purpose |
|--------|---------|
| `GetScriptModule` | Get current script module |
| `GetWBScriptModule` | Get Workbench script module |
| `GetWBGameScriptModule` | Get Workbench game module |

## File/Path Conventions

### Project Files

Script modules are defined in `.sproj` files:
```
scripts/projects/Engine.sproj
scripts/projects/Entities.sproj
scripts/projects/GameLib.sproj
scripts/projects/Game.sproj
scripts/projects/Workbench.sproj        (editor only)
scripts/projects/WorkbenchGame.sproj    (editor only)
```

### Resource Path Syntax

Module paths use the `@"path"` syntax for compiler references:
- `Compilation failed for @"%s"` - File path in error
- `@"%s;%s,%d"` - Resource path with parameters

### Script Directories

Standard script directory structure:
- `scripts/Game/` - Game module scripts
- `scripts/GameLib/` - GameLib module scripts

## Native Code Binding

### Script Registration

| Component | Purpose |
|-----------|---------|
| `ScriptRegistrator` | Registers C++ classes to script |
| `ClassRegistrator` | Individual class registration |
| `RegisterScriptClasses` | Bulk class registration method |
| `GenerateScriptDeclaration` | Generates script declarations |

### Declaration Generation Errors

| Error | Meaning |
|-------|---------|
| `ScriptRegistrator::GenerateScriptDeclaration: directory for script module '%s' is not present in Enfusion Data` | Missing module directory |
| `ScriptRegistrator::GenerateScriptDeclaration: directory for script module '%s' is not present in Game Data` | Missing game data directory |
| `Generating scripts declarations file '%s' failed` | Declaration generation failed |
| `Config class '%s' hasn't script declaration and can't be instantiated` | Class not scriptable |

### Native Method Binding

| Error | Meaning |
|-------|---------|
| `Method '%s' is linked as member but declared as external/static.` | Linkage mismatch |
| `Method '%s' is linked as static/external but declared as member.` | Linkage mismatch |
| `Method '%s.%s' methods marked as 'native' are not supported.` | Native method limitation |
| `Error in script binding: class/enum '%s' declaration is missing in script!` | Missing binding |

## Module Validation and Checksums

### Script Source Validation

For multiplayer replication, script checksums are validated:
- `RplConnection::ValidationError remote script source code checksum does not match! local=0x%llX remote=0x%llX`

This ensures all players have identical script code.

### Class Layout Validation

- `RplLayoutError: could not find script layout. nodeId=0x%08X, classHash=0x%08X`

Classes must have matching layouts for replication.

### RDB Checksum

- `RplConnection::ValidationError remote rdb checksum does not match! local=0x%llX remote=0x%llX`

Resource database checksums must match.

## Module System for Mods

### Addon Scripts

Mods can add scripts that integrate with the module system:
- `Addon cannot be packed due to failed script compilation!`

### Modded Classes

- `Sealed type '%s' can't be modded` - Some classes cannot be modified
- `modded` keyword allows extending classes

Regex pattern for class parsing: `^(\s*\bmodded\b|\s*\bsealed\b)*\s*(\bclass\b|\benum\b)+\s(\w+)`

## Entity Creation from Modules

### Module-Based Instantiation

Error: `Failed to create entity. scriptModule->New() returned null`

Entities are created through their module's `New()` method, ensuring proper module context.

## Summary

The Enforce Script module system:

1. **Organizes code** into hierarchical modules (Engine -> Entities -> GameLib -> Game)
2. **Enforces dependencies** - lower modules cannot depend on higher ones
3. **Compiles in order** - respecting module dependencies
4. **Validates types** - types must be declared in their proper module
5. **Binds native code** - C++ classes registered to script modules
6. **Validates checksums** - multiplayer requires matching script versions
7. **Supports mods** - addons can extend modules (except sealed types)

Understanding module boundaries is critical for writing correct Enforce Script code, especially for cross-module class access and inheritance.
