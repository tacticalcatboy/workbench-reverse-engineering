# Progress Check - Where Are We?

I'm continuing a Workbench reverse-engineering project. Help me understand current progress and determine next steps.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

## Read These Files First

1. `docs/getting-started/checklist.md` - Current progress tracking
2. `docs/session-log.md` - History of what's been done
3. `docs/strategy.md` - Project goals and phases

## Questions to Answer

### 1. Current Phase Status
- Which research phases are complete?
- Which are in progress?
- Which haven't started?

### 2. Key Metrics
Report current counts for:
- Diagnostic patterns found
- API classes discovered
- Keywords confirmed
- Strings analyzed

### 3. Open Questions
What research questions remain unanswered? Check:
- `docs/getting-started/checklist.md` (Research Questions section)
- `docs/findings/*.md` files (look for "Unknown" or "Needs Research" sections)

### 4. Blockers or Gaps
Identify any:
- Missing data that blocks progress
- Tools needed but not set up
- Areas that need deeper investigation

### 5. Recommended Next Steps
Based on current state, suggest 3-5 concrete next actions, prioritized by:
- Impact on project goals (helping AI write better Enforce Script)
- Effort required
- Dependencies on other work

## Output Format

Provide a summary like:

```
## Progress Report

### Completed
- [list completed items]

### In Progress
- [list in-progress items]

### Not Started
- [list planned items]

### Key Stats
| Metric | Count |
|--------|-------|
| ... | ... |

### Open Questions
1. ...
2. ...

### Recommended Next Steps
1. [High priority] ...
2. [Medium priority] ...
3. [Low priority] ...

### Blockers
- [any blockers or none]
```

## After Review

If the user wants to proceed with a specific task:
1. Check if a prompt exists in `prompts/` for that task
2. If yes, suggest using that prompt
3. If no, offer to create one

Available prompts:
- `prompts/extract-api-signatures.md` - API method extraction
- `prompts/dll-analysis.md` - DLL file analysis
- `prompts/progress-check.md` - This prompt
