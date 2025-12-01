# 03 - Enhance AI Linter with Parsed Data

Upgrade the AI linter prompt with structured API data for accurate code review.

## Context

- **Input:** Parsed JSON from `01-parse-api-docs.md`
- **Output:** Enhanced `prompts/ai-linter.md` with real API knowledge
- **Purpose:** Transform "soft linter" into data-backed validator

## Prerequisites

- Complete `01-parse-api-docs.md` (JSON API data exists)
- Complete `02-create-cli-tool.md` (CLI tool exists)

## Current State

The existing `prompts/ai-linter.md` has:
- General language knowledge
- Common error patterns
- Basic review guidelines

Missing:
- Actual class names (8,704 classes)
- Real method signatures
- Accurate inheritance information
- Component types and their methods

## Task

### Step 1: Create API Reference Appendix

Generate `prompts/api-reference.md` with:

#### Common Base Classes
```markdown
## ScriptComponent
Methods:
- void EOnInit(IEntity owner)
- void EOnFrame(IEntity owner, float timeSlice)
- void EOnActivate(IEntity owner)
- void EOnDeactivate(IEntity owner)
- IEntity GetOwner()
- T FindComponent<T>(typename)
```

#### Most-Used Classes (Top 100)
Extract from parsed JSON based on:
- Base component classes
- Entity types
- Manager classes
- UI/Widget classes
- RPC-enabled classes

### Step 2: Create Inheritance Quick Reference

Generate `prompts/inheritance-ref.md`:

```markdown
## Sealed Classes (Cannot Extend)
- SealedClass1
- SealedClass2

## Abstract Classes (Must Extend)
- AbstractBase1
- AbstractBase2

## Common Inheritance Chains
ScriptComponent → BaseComponent → ComponentBase
GenericEntity → IEntity → EntityBase
```

### Step 3: Update AI Linter Prompt

Modify `prompts/ai-linter.md` to:

1. **Reference the appendices**
   ```
   Refer to prompts/api-reference.md for method signatures.
   Refer to prompts/inheritance-ref.md for class hierarchy.
   ```

2. **Add specific validation rules**
   ```
   When you see FindComponent<T>:
   - Verify T is a valid component type (see api-reference.md)
   - Always check for null before using result
   - Common components: SCR_*, Base*, Generic*
   ```

3. **Include real error message templates**
   ```
   Real compiler messages:
   - "class '%s' cannot extend sealed class '%s'"
   - "method '%s' has wrong return type, expected '%s' actual '%s'"
   - "Cannot convert '%s' to '%s'"
   ```

### Step 4: Create Focused Sub-Prompts

Split into specialized prompts:

#### `prompts/linter-components.md`
Focus: ScriptComponent, EntityComponent validation

#### `prompts/linter-rpc.md`
Focus: RPC methods, replication, networking

#### `prompts/linter-ui.md`
Focus: Widget classes, UI handlers, events

### Step 5: Generate Statistics Summary

Add to linter prompt:
```
## API Statistics
- Total Classes: 8,704
- Enfusion Core: 824
- Arma Reforger: 7,880
- RPC Methods: 373+
- Event Handlers: 60+
```

## Output Structure

```
docs/prompts/
├── ai-linter.md              # Main prompt (updated)
├── api-reference.md          # Top 100 classes with signatures
├── inheritance-ref.md        # Class hierarchy reference
├── linter-components.md      # Component-specific rules
├── linter-rpc.md             # RPC-specific rules
└── linter-ui.md              # UI-specific rules
```

## Validation

Test enhanced linter against:
1. Code using real API classes
2. Common error patterns
3. Edge cases from our research

## Next Prompt

After completing this task, proceed to `04-ai-workflow.md`
