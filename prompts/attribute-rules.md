# Attribute Parameter Rules

I'm continuing a Workbench reverse-engineering project to document Enforce Script attribute validation rules.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. docs/findings/api.md - Known attributes (20+ types)
2. docs/findings/keywords.md - Attribute syntax evidence
3. docs/findings/diagnostics.md - Attribute-related errors

## Context

We know attributes use square bracket syntax: `[AttributeName]`

Known attributes:
- `[EventAttribute]` - Marks event methods
- `[ReceiverAttribute]` - Marks receiver methods
- `[RplRpc]` - Marks RPC methods
- `[ButtonAttribute]` - UI buttons
- Various data attributes (AimingModifierAttributes, AttachmentAttributes, etc.)

## Analysis Tasks

### Task 1: Attribute Error Messages
Search for all attribute-related error messages:

```
Patterns:
- "attribute" (case insensitive)
- "Attribute]"
- "[" followed by capital letter
- "marked with"
- "missing attribute"
```

### Task 2: Attribute Types
Categorize discovered attributes:

| Category | Attributes | Purpose |
|----------|-----------|---------|
| Method | EventAttribute, ReceiverAttribute, RplRpc | Mark method types |
| Class | ? | Class-level attributes |
| Property | ? | Property attributes |
| Serialization | ? | Serialization control |
| UI | ButtonAttribute | UI elements |
| Data | *Attributes classes | Configuration |

### Task 3: Parameter Validation
Document what parameters each attribute accepts:

```
[AttributeName]              - No parameters
[AttributeName(value)]       - Single positional
[AttributeName(a, b)]        - Multiple positional
[AttributeName(name=value)]  - Named parameter
[AttributeName(a, name=b)]   - Mixed
```

Look for error messages revealing:
- Required vs optional parameters
- Parameter types (string, int, bool, enum)
- Valid value ranges
- Parameter name requirements

### Task 4: Placement Rules
Document where attributes can be placed:
- Before class declarations
- Before method declarations
- Before property declarations
- Before parameters
- Multiple attributes on same target

### Task 5: Attribute Inheritance
Check if attributes are inherited:
- Does a subclass inherit parent's attributes?
- Can attributes be overridden?
- Attribute conflicts in inheritance

## Search Patterns

```bash
# Attribute errors
grep -i "attribute" data/workbench/all_strings.txt
grep -i "marked with" data/workbench/all_strings.txt

# Specific attributes
grep -i "EventAttribute" data/workbench/all_strings.txt
grep -i "RplRpc" data/workbench/all_strings.txt
grep -i "Receiver" data/workbench/all_strings.txt

# Attribute parameters
grep -i "parameter.*attribute" data/workbench/all_strings.txt
grep -i "attribute.*parameter" data/workbench/all_strings.txt
```

## Known Attribute Errors

From previous research:
- `Method '%s.%s' is not marked with the [EventAttribute] attribute`
- `Method '%s.%s' is not marked with the [ReceiverAttribute] attribute`
- `Method '%s.%s' methods marked as 'native' are not supported`
- `RpcError: Could not find the RPC. Are you missing the RplRpc attribute?`

## Output

### Create:
- `docs/reference/attributes.md` - Complete attribute reference

### Document for each attribute:
- Name and syntax
- Where it can be placed
- Required parameters
- Optional parameters with defaults
- Valid parameter values
- Related error messages
- Example usage

### Update:
- `docs/findings/api.md` - Add any new attributes discovered
- `docs/getting-started/checklist.md` - Mark task complete

## Goal

Create an attribute reference sufficient for:
1. AI to correctly apply attributes
2. Understanding attribute requirements
3. Predicting validation errors

## When Complete

Update `docs/getting-started/checklist.md`:
- Move "Document attribute parameter rules" to Completed
