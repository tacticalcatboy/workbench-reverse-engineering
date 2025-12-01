# Property Extraction

I'm continuing a Workbench reverse-engineering project to extract property names and accessor patterns from Enforce Script.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/findings/api.md - Current API surface (1,833 classes, methods found so far)
2. docs/getting-started/checklist.md - Progress tracking

## Context

Phase 2 requires extracting property names. We have class names (1,833) but property information is incomplete.

Properties in C#-like languages typically follow patterns:
- Getter: `GetPropertyName()` or `get_PropertyName()`
- Setter: `SetPropertyName(value)` or `set_PropertyName(value)`
- Boolean: `IsPropertyName()`, `HasPropertyName()`, `CanPropertyName()`
- Direct access may also exist

## Data Sources

- `data/workbench/all_strings.txt` (84,718 strings)
- `data/game/game_all_strings.txt` (61,575 strings)

## Analysis Tasks

### Task 1: Getter Pattern Extraction

Search for getter patterns:

```bash
# Standard getters
grep -E "^Get[A-Z]" data/workbench/all_strings.txt | sort -u
grep -E "\.Get[A-Z]" data/workbench/all_strings.txt | sort -u

# Underscore style
grep -E "get_[A-Z]" data/workbench/all_strings.txt | sort -u

# In error messages
grep -E "Get[A-Z][a-zA-Z]*'" data/workbench/all_strings.txt
```

### Task 2: Setter Pattern Extraction

Search for setter patterns:

```bash
# Standard setters
grep -E "^Set[A-Z]" data/workbench/all_strings.txt | sort -u
grep -E "\.Set[A-Z]" data/workbench/all_strings.txt | sort -u

# Underscore style
grep -E "set_[A-Z]" data/workbench/all_strings.txt | sort -u
```

### Task 3: Boolean Property Patterns

Search for boolean accessors:

```bash
# Is* pattern
grep -E "^Is[A-Z]" data/workbench/all_strings.txt | sort -u
grep -E "\.Is[A-Z]" data/workbench/all_strings.txt | sort -u

# Has* pattern
grep -E "^Has[A-Z]" data/workbench/all_strings.txt | sort -u
grep -E "\.Has[A-Z]" data/workbench/all_strings.txt | sort -u

# Can* pattern
grep -E "^Can[A-Z]" data/workbench/all_strings.txt | sort -u
grep -E "\.Can[A-Z]" data/workbench/all_strings.txt | sort -u

# Should* pattern
grep -E "^Should[A-Z]" data/workbench/all_strings.txt | sort -u
```

### Task 4: Property Error Messages

Look for property-related errors that reveal property names:

```bash
# Property errors
grep -i "property" data/workbench/all_strings.txt
grep -i "Property '%s'" data/workbench/all_strings.txt

# Member access errors
grep -i "member '%s'" data/workbench/all_strings.txt
grep -i "field '%s'" data/workbench/all_strings.txt

# Replicated properties
grep -i "replicated property" data/workbench/all_strings.txt
```

### Task 5: Class.Property Pairs

Extract property names associated with specific classes:

```bash
# Look for Class.Property patterns
grep -E "[A-Z][a-zA-Z]+\.(Get|Set|Is|Has)[A-Z]" data/workbench/all_strings.txt

# Component properties
grep -E "Component\.(Get|Set)" data/workbench/all_strings.txt

# Entity properties
grep -E "Entity\.(Get|Set)" data/workbench/all_strings.txt
```

### Task 6: Categorize by Domain

Group properties by system:

| Domain | Patterns to Search |
|--------|-------------------|
| Transform | Position, Rotation, Scale, Transform, Origin |
| Physics | Velocity, Mass, Force, Impulse, Collision |
| Rendering | Visible, Color, Material, Texture, Mesh |
| Audio | Volume, Pitch, Sound, Audio |
| Network | Replicated, Synced, Owner, Authority |
| Gameplay | Health, Damage, Ammo, Inventory, Action |
| AI | Target, Waypoint, Behavior, State |
| UI | Widget, Text, Image, Button, Layout |

```bash
# Example: Transform properties
grep -iE "(Get|Set|Is|Has).*(Position|Rotation|Scale|Transform)" data/workbench/all_strings.txt
```

### Task 7: Paired Getter/Setter Analysis

Identify properties that have both getter and setter:

```bash
# Extract all Get* methods
grep -oE "Get[A-Z][a-zA-Z]+" data/workbench/all_strings.txt | sort -u > /tmp/getters.txt

# Extract all Set* methods
grep -oE "Set[A-Z][a-zA-Z]+" data/workbench/all_strings.txt | sort -u > /tmp/setters.txt

# Find matches (Get*/Set* pairs indicate read-write properties)
# GetFoo -> SetFoo means Foo is read-write
```

## Output Format

### Create: `docs/findings/properties.md`

Structure:
```markdown
# Properties

## Statistics
| Category | Count |
|----------|-------|
| Getters | X |
| Setters | X |
| Boolean (Is/Has/Can) | X |
| Read-only (Get only) | X |
| Read-write (Get+Set) | X |

## By Domain

### Transform Properties
| Property | Getter | Setter | Type (if known) |
|----------|--------|--------|-----------------|
| Position | GetPosition | SetPosition | vector |
| ... | ... | ... | ... |

### Entity Properties
...

### Component Properties
...

## By Class

### IEntity
- GetWorld()
- GetOrigin() / SetOrigin()
- GetYawPitchRoll() / SetYawPitchRoll()
...

### GenericComponent
...
```

### Update:
- `docs/findings/api.md` - Add property section or link to new file
- `docs/getting-started/checklist.md` - Add "Extract property names" to completed

## Expected Discoveries

Common property categories:
1. **Entity properties** - Position, rotation, parent, children
2. **Component properties** - Owner, enabled state
3. **Physics properties** - Velocity, mass, collision
4. **Visual properties** - Visibility, materials
5. **Network properties** - Replication state, ownership
6. **Gameplay properties** - Health, damage, inventory

## Success Criteria

Phase 2 property extraction complete when:
- [ ] 100+ unique properties documented
- [ ] Properties grouped by class/domain
- [ ] Getter/setter pairs identified
- [ ] Read-only vs read-write distinguished
- [ ] Types documented where discoverable

## When Complete

Update `docs/strategy.md`:
- Mark "Extract property names" as complete in Phase 2
