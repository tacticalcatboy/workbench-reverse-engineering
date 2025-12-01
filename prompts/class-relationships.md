# Class Relationship Mapping

I'm continuing a Workbench reverse-engineering project to map class relationships (inheritance, composition, dependencies) in Enforce Script.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/findings/api.md - 1,833 ClassRegistrator entries, component systems
2. docs/findings/keywords.md - Class modifiers (sealed, modded, abstract)
3. docs/reference/ast-nodes.md - ClassDefNode structure

## Context

Phase 2 requires mapping class relationships. We have 1,833 class names but don't know:
- Which classes inherit from which
- Required base classes for different systems
- Composition patterns (which components go together)
- Module dependencies

## Data Sources

- `data/workbench/all_strings.txt` (84,718 strings)
- `data/game/game_all_strings.txt` (61,575 strings)

## Analysis Tasks

### Task 1: Inheritance Error Messages

Extract inheritance information from error messages:

```bash
# Direct inheritance errors
grep -i "inherit" data/workbench/all_strings.txt
grep -i "derive" data/workbench/all_strings.txt
grep -i "base class" data/workbench/all_strings.txt

# Specific patterns found previously
grep "cannot derive from" data/workbench/all_strings.txt
grep "must inherit from" data/workbench/all_strings.txt
grep "Circle inheritance" data/workbench/all_strings.txt
```

### Task 2: Required Base Classes

Find which systems require specific base classes:

```bash
# Component requirements
grep -i "Component.*must inherit" data/workbench/all_strings.txt
grep -i "must inherit.*Component" data/workbench/all_strings.txt

# Entity requirements
grep -i "Entity.*must inherit" data/workbench/all_strings.txt
grep -i "must inherit.*Entity" data/workbench/all_strings.txt

# Script class requirements
grep -i "Script class must" data/workbench/all_strings.txt

# Generic inheritance requirements
grep -E "Class '%s' must inherit from '%s'" data/workbench/all_strings.txt
grep -E "'%s' must be inherited from" data/workbench/all_strings.txt
```

### Task 3: Sealed/Abstract Classes

Find sealed and abstract class patterns:

```bash
# Sealed classes (cannot be extended)
grep -i "sealed" data/workbench/all_strings.txt
grep "cannot derive from sealed" data/workbench/all_strings.txt
grep "Sealed type.*can't be modded" data/workbench/all_strings.txt

# Abstract classes
grep -i "abstract" data/workbench/all_strings.txt
grep "abstract.*cannot be created" data/workbench/all_strings.txt
```

### Task 4: Interface-like Patterns

Check for interface or protocol patterns:

```bash
# Interface naming convention
grep -E "^I[A-Z][a-zA-Z]+" data/workbench/all_strings.txt | head -50

# Implementation patterns
grep -i "implement" data/workbench/all_strings.txt
grep -i "interface" data/workbench/all_strings.txt
```

### Task 5: Composition Patterns

Find which classes contain/use other classes:

```bash
# Component composition
grep -E "[A-Z]+Component" data/workbench/all_strings.txt | sort -u

# FindComponent usage (reveals what components are looked up)
grep "FindComponent" data/workbench/all_strings.txt

# Required components
grep -i "requires.*component" data/workbench/all_strings.txt
grep -i "missing.*component" data/workbench/all_strings.txt

# Has/Contains patterns
grep -E "(Has|Contains)[A-Z][a-zA-Z]*Component" data/workbench/all_strings.txt
```

### Task 6: Module Dependencies

Map cross-module relationships:

```bash
# Module references
grep -E "(Engine|Entities|GameLib|Game|Workbench)" data/workbench/all_strings.txt | grep -i "module\|import\|depend"

# Namespace relationships
grep -E "@(enf|gamelib|gamecode|ailib)" data/workbench/all_strings.txt
```

### Task 7: Class Hierarchies by System

Document hierarchies for major systems:

**Entity System:**
```bash
grep -E "(Entity|IEntity|GenericEntity)" data/workbench/all_strings.txt
```

**Component System:**
```bash
grep -E "(Component|GenericComponent|ScriptComponent)" data/workbench/all_strings.txt
```

**Controller System:**
```bash
grep -E "(Controller|PlayerController|AIController)" data/workbench/all_strings.txt
```

**Manager System:**
```bash
grep -E "Manager" data/workbench/all_strings.txt | grep -E "^[A-Z]" | sort -u
```

### Task 8: Override Chains

Find methods that must be overridden:

```bash
# Override requirements
grep -i "override" data/workbench/all_strings.txt
grep "must.*override" data/workbench/all_strings.txt
grep "marked as override" data/workbench/all_strings.txt

# Virtual/abstract method hints
grep -i "virtual" data/workbench/all_strings.txt
```

### Task 9: Type Compatibility

Find which types can be converted/cast to others:

```bash
# Cast errors
grep -i "cannot cast" data/workbench/all_strings.txt
grep -i "Cannot convert" data/workbench/all_strings.txt
grep "incompatible type" data/workbench/all_strings.txt

# Type relationships
grep -E "type '%s'.*type '%s'" data/workbench/all_strings.txt
```

## Output Format

### Create: `docs/findings/class-hierarchy.md`

Structure:
```markdown
# Class Hierarchy

## Core Hierarchies

### Entity Hierarchy
```
Object (root)
└── IEntity
    └── GenericEntity
        ├── Building
        ├── Vehicle
        ├── Character
        └── ...
```

### Component Hierarchy
```
GenericComponent
├── ScriptComponent
├── ScriptedGameTriggerEntity
└── ...
```

## Inheritance Requirements

| System | Required Base Class | Evidence |
|--------|--------------------| ---------|
| Entities | GenericEntity | "must inherit from GenericEntity" |
| Components | GenericComponent | Error message X |
| ... | ... | ... |

## Sealed Classes (Cannot Extend)
- ClassName - Reason/evidence

## Abstract Classes (Must Extend)
- ClassName - Purpose

## Common Composition Patterns

### Character Entity
Typical components:
- CharacterControllerComponent
- CharacterAnimationComponent
- InventoryStorageManagerComponent
- ...

### Vehicle Entity
Typical components:
- VehicleControllerComponent
- ...

## Module Dependencies

```
Engine (core)
└── Entities
    └── GameLib
        └── Game
            └── Workbench (editor only)
```

## Interface-like Classes
Classes starting with 'I' that define contracts:
- IEntity
- IComponent
- ...
```

### Update:
- `docs/findings/api.md` - Link to hierarchy documentation
- `docs/strategy.md` - Mark "Map relationships" complete in Phase 2
- `docs/getting-started/checklist.md` - Add to completed items

## Known Relationships (from previous research)

From `api.md`:
- `Component Class '%s' must inherit from '%s'`
- `Entity Class '%s' must inherit from '%s'`
- `Game::SpawnEntity: Class must inherits from GenericEntity!`
- `Script class must be inherited from BaseLoadingAnim`
- `Can't inherit class '%s'`
- `Circle inheritance in class '%s'`

## Success Criteria

Phase 2 relationship mapping complete when:
- [ ] Core entity hierarchy documented
- [ ] Core component hierarchy documented
- [ ] 20+ inheritance requirements documented
- [ ] Sealed/abstract classes identified
- [ ] Common composition patterns documented
- [ ] Module dependency graph created

## When Complete

Update `docs/strategy.md`:
- Mark "Map relationships" as complete in Phase 2

This completes Phase 2: API Surface Discovery.
