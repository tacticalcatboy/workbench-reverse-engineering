# AI Linter Prompts

System prompts for AI-powered Enforce Script code review.

## Quick Start

**Use `ai-linter.md`** - This is the main prompt containing everything needed for general code review.

## Validation Rules (JSON)

Machine-readable validation rules in `data/validation/`:

| File | Purpose |
|------|---------|
| `tokens.json` | Keywords, operators, literals, comments |
| `grammar-rules.json` | BNF syntax rules, AST patterns |
| `type-rules.json` | Type system, conversions, operators |
| `error-patterns.json` | Error codes E001-E140, warnings W001-W012 |

These JSON files enable deterministic validation. The prompts below use them for AI-assisted review.

## File Structure

```
linter/
├── index.md                 # This file - overview
├── ai-linter.md             # MAIN PROMPT - use this for general review
├── claude-md-snippet.md     # COPY THIS into your project's CLAUDE.md
│
├── Reference Data (included in main prompt):
│   ├── api-reference.md     # Class/method signatures
│   └── inheritance-ref.md   # Class hierarchy
│
└── Specialized Prompts (use instead of main for focused review):
    ├── linter-components.md # Component-specific validation
    ├── linter-rpc.md        # RPC/networking validation
    └── linter-ui.md         # Widget/UI validation

data/validation/             # Machine-readable rules
├── tokens.json
├── grammar-rules.json
├── type-rules.json
├── error-patterns.json
└── README.md
```

## Quick Integration

**To add linting to your Enforce Script project:**

1. Open `claude-md-snippet.md`
2. Copy the snippet section
3. Paste into your project's `CLAUDE.md`
4. Claude will now lint your `.c` files automatically

## When to Use What

| File | Use When |
|------|----------|
| `ai-linter.md` | General code review, most situations |
| `linter-components.md` | Reviewing ScriptComponent, EOn* events, FindComponent |
| `linter-rpc.md` | Reviewing networked code, [RplRpc], replication |
| `linter-ui.md` | Reviewing Widget handlers, menus, UI code |

## Reference Files

These aren't prompts - they're data appendices:

- **`api-reference.md`** - Method signatures for 100+ common classes
- **`inheritance-ref.md`** - Class hierarchy trees and inheritance rules

The main `ai-linter.md` prompt already includes the key information from these. Use them for deeper lookup.

## Usage Examples

### General Review
```
Use ai-linter.md as system prompt, then:
"Review this code: [paste code]"
```

### Component-Focused Review
```
Use linter-components.md as system prompt, then:
"Review this component: [paste ScriptComponent code]"
```

### RPC-Focused Review
```
Use linter-rpc.md as system prompt, then:
"Review this networked code: [paste RPC code]"
```
