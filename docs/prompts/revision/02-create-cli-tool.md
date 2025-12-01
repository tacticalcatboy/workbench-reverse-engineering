# 02 - Create CLI Validation Tool

Create a command-line tool that AI can invoke to validate Enforce Script code.

## Context

- **Input:** Enforce Script source files (`.c` files)
- **Output:** JSON with errors, warnings, hints
- **Purpose:** Give AI a tool to validate code without Workbench

## Prerequisites

- Complete `01-parse-api-docs.md` first
- JSON API data available in `data/api/`

## Task

### Step 1: Design CLI Interface

Create `tools/enforce-lint/` with this interface:

```bash
# Validate a single file
enforce-lint check script.c

# Validate a directory
enforce-lint check scripts/Game/

# Output formats
enforce-lint check script.c --format json
enforce-lint check script.c --format text

# Specific checks only
enforce-lint check script.c --only syntax
enforce-lint check script.c --only types
enforce-lint check script.c --only api
```

### Step 2: Implement Core Validators

Create validators based on our reverse-engineered knowledge:

#### 2a. Syntax Validator
- Bracket matching
- Semicolon presence
- String literal closure
- Comment closure

#### 2b. Class Validator
Using `data/diagnostics.md` patterns:
- `class '%s' cannot extend sealed class '%s'`
- `Circular class inheritance`
- `method '%s' cannot override, not marked as 'override'`

#### 2c. API Validator
Using `data/api/*.json`:
- Method exists on class
- Correct parameter count
- Parameter types match (basic)
- Return type usage

#### 2d. Pattern Validator
Common mistakes from our research:
- Null checks before method calls
- `override` keyword on EOn* methods
- RPC method naming conventions

### Step 3: Output Format

```json
{
  "file": "scripts/Game/MyComponent.c",
  "success": false,
  "errors": [
    {
      "line": 15,
      "column": 8,
      "code": "E001",
      "severity": "error",
      "message": "Method 'DoSomething' not found on class 'BaseComponent'",
      "suggestion": "Did you mean 'DoAction'?"
    }
  ],
  "warnings": [
    {
      "line": 10,
      "column": 4,
      "code": "W001",
      "severity": "warning",
      "message": "EOnInit missing 'override' keyword"
    }
  ],
  "hints": [
    {
      "line": 20,
      "column": 1,
      "code": "H001",
      "severity": "hint",
      "message": "Variable 'temp' can be const"
    }
  ]
}
```

### Step 4: Error Code Registry

Create `tools/enforce-lint/error-codes.json`:

```json
{
  "E001": {"category": "api", "message": "Method not found"},
  "E002": {"category": "api", "message": "Wrong parameter count"},
  "E003": {"category": "inheritance", "message": "Cannot extend sealed class"},
  "W001": {"category": "override", "message": "Missing override keyword"},
  "W002": {"category": "null-safety", "message": "Potential null reference"},
  "H001": {"category": "const", "message": "Variable can be const"}
}
```

## Tech Stack

Recommended: **Python** for quick iteration
- argparse for CLI
- JSON for output
- Regex-based parsing (no full parser needed initially)

Alternative: **Node.js/TypeScript** for better async and future LSP

## Expected Output Structure

```
tools/
└── enforce-lint/
    ├── __main__.py           # CLI entry point
    ├── validators/
    │   ├── syntax.py
    │   ├── classes.py
    │   ├── api.py
    │   └── patterns.py
    ├── error-codes.json
    └── README.md
```

## Testing

Test with known-bad code samples:
1. Missing override keyword
2. Calling method on null
3. Wrong parameter count
4. Extending sealed class

## Next Prompt

After completing this task, proceed to `03-enhance-ai-linter.md`
