# 04 - AI Workflow Documentation

Document the complete AI coding workflow with all tools integrated.

## Context

- **Input:** All previous prompts completed
- **Output:** Comprehensive workflow documentation
- **Purpose:** Enable AI to effectively write and validate Enforce Script

## Prerequisites

- `01-parse-api-docs.md` complete (JSON data exists)
- `02-create-cli-tool.md` complete (CLI tool exists)
- `03-enhance-ai-linter.md` complete (Enhanced prompts exist)

## Task

### Step 1: Create Workflow Overview

Create `docs/ai-workflow.md`:

```markdown
# AI Enforce Script Workflow

## Overview

This workflow enables AI to write, validate, and iterate on Enforce Script code
without requiring Workbench compilation.

## Components

1. **AI Linter Prompt** - Soft validation during writing
2. **CLI Tool** - Hard validation after writing
3. **API Reference** - Autocomplete and signature lookup
4. **Error Patterns** - Known issues and fixes

## The Loop

┌─────────────┐
│  AI writes  │
│    code     │
└─────┬───────┘
      │
      ▼
┌─────────────┐     Pass      ┌─────────────┐
│  CLI tool   │──────────────>│    Done     │
│   checks    │               └─────────────┘
└─────┬───────┘
      │ Fail
      ▼
┌─────────────┐
│  AI reads   │
│   errors    │
└─────┬───────┘
      │
      ▼
┌─────────────┐
│  AI fixes   │
│   issues    │
└─────┬───────┘
      │
      └──────────> (back to CLI check)
```

### Step 2: Document Tool Integration

#### For Claude/AI Systems

```markdown
## System Prompt Integration

Add to your AI system prompt:

1. Include `prompts/ai-linter.md` for code review knowledge
2. Reference `prompts/api-reference.md` for class lookups
3. After writing code, invoke:
   ```bash
   enforce-lint check <file> --format json
   ```
4. Parse JSON output and fix any errors
5. Repeat until `success: true`
```

#### For IDE Extensions

```markdown
## VSCode Integration

1. Create task in `.vscode/tasks.json`:
   ```json
   {
     "label": "Enforce Lint",
     "type": "shell",
     "command": "python",
     "args": ["tools/enforce-lint", "check", "${file}", "--format", "json"]
   }
   ```

2. Use output for Problems panel
```

### Step 3: Create Quick Reference Card

Create `docs/prompts/quick-reference.md`:

```markdown
# Enforce Script Quick Reference

## Common Classes
| Class | Purpose | Key Methods |
|-------|---------|-------------|
| ScriptComponent | Base for components | EOnInit, FindComponent |
| GenericEntity | Base for entities | GetWorld, FindComponent |
| SCR_* | Game-specific | Varies |

## Common Patterns

### Component Access
```csharp
SomeComponent comp = SomeComponent.Cast(FindComponent(SomeComponent));
if (comp)
    comp.DoSomething();
```

### RPC Call
```csharp
[RplRpc(RplChannel.Reliable, RplRcver.Server)]
protected void Rpc_DoAction_S(int param)
{
    // Server-side code
}
```

### Event Handler
```csharp
override void EOnInit(IEntity owner)
{
    // Initialize
}
```

## Error Quick Fixes

| Error | Fix |
|-------|-----|
| Missing override | Add `override` keyword |
| Null reference | Add null check |
| Wrong param count | Check API reference |
| Cannot extend sealed | Use composition instead |
```

### Step 4: Create Troubleshooting Guide

Create `docs/troubleshooting.md`:

```markdown
# Troubleshooting

## CLI Tool Issues

### "Class not found in API"
- Check spelling
- May be game-specific (SCR_*) vs engine
- Check inheritance chain

### "Method signature mismatch"
- Verify parameter types
- Check if method is static
- Confirm correct overload

## Common AI Mistakes

### Over-engineering
- Keep code simple
- Don't add unnecessary abstractions
- Match existing code style

### Missing Null Checks
- Always check FindComponent results
- Validate entity references
- Handle edge cases
```

### Step 5: Update Main Documentation

Update these files:
- `docs/index.md` - Add workflow section
- `docs/strategy.md` - Reference new workflow
- `mkdocs.yml` - Add new pages to navigation

## Output Structure

```
docs/
├── ai-workflow.md           # Main workflow documentation
├── troubleshooting.md       # Common issues and fixes
├── prompts/
│   ├── quick-reference.md   # Cheat sheet for AI
│   └── ...
└── mkdocs.yml               # Updated navigation
```

## Final Validation

1. Walk through complete workflow manually
2. Test with sample code
3. Verify all documentation links work
4. Ensure consistent terminology

## Completion Checklist

- [ ] AI workflow documented
- [ ] Tool integration documented
- [ ] Quick reference created
- [ ] Troubleshooting guide created
- [ ] Navigation updated
- [ ] All cross-references valid
