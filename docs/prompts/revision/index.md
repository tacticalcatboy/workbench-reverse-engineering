# Revision Prompts

Step-by-step prompts to build AI tooling for Enforce Script.

## Purpose

These prompts guide AI (or developers) through building a complete validation and linting system for Enforce Script, without requiring Workbench compilation.

## Execution Order

| # | Prompt | Description | Depends On |
|---|--------|-------------|------------|
| 01 | [Parse API Docs](01-parse-api-docs.md) | Convert Doxygen HTML to JSON | None |
| 02 | [Create CLI Tool](02-create-cli-tool.md) | Build validation CLI | 01 |
| 03 | [Enhance AI Linter](03-enhance-ai-linter.md) | Upgrade linter with real data | 01, 02 |
| 04 | [AI Workflow](04-ai-workflow.md) | Document complete workflow | 01, 02, 03 |
| 05 | [Enforce Validator](05-enforce-validator.md) | **Replicate Workbench validator** | 01 |

## How to Use

1. Start with prompt 01 and complete fully
2. Proceed to next prompt only after previous is done
3. Each prompt has validation steps - don't skip them
4. Update documentation as you go

## Expected Outcomes

After completing all prompts:

- **8,704 classes** parsed into JSON
- **CLI tool** for offline validation
- **Enhanced prompts** with real API data
- **Complete workflow** for AI coding
- **Standalone validator** matching Workbench behavior

## Time Estimate

| Prompt | Estimated Effort |
|--------|-----------------|
| 01 | Medium (parsing logic) |
| 02 | High (CLI + validators) |
| 03 | Medium (prompt writing) |
| 04 | Low (documentation) |
| 05 | **High** (lexer + parser + analyzer) |

## Notes

- These prompts are designed for AI execution but work for humans too
- Each prompt is self-contained with all needed context
- Validation steps ensure quality before proceeding
- Output locations are specified - follow them for consistency
