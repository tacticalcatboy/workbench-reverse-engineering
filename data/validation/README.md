# Enforce Script Validation Rules

Machine-readable validation rules for Enforce Script syntax checking and linting.

## Files

| File | Purpose |
|------|---------|
| `tokens.json` | Lexical rules (keywords, operators, literals, comments) |
| `grammar-rules.json` | Syntax rules (BNF patterns, AST nodes, declaration/statement rules) |
| `type-rules.json` | Type system rules (primitives, generics, reference modifiers, conversions) |
| `error-patterns.json` | Diagnostic patterns (error codes, messages, severity levels) |

## Usage

### Tokenization (tokens.json)

Use for lexical analysis - splitting source code into tokens.

```json
{
  "keywords": {
    "control_flow": ["if", "else", "for", ...],
    "class_modifiers": ["class", "sealed", "modded", ...],
    ...
  },
  "operators": {
    "arithmetic": ["+", "-", "*", "/", "%"],
    "comparison": ["==", "!=", "<", ">", ...],
    ...
  },
  "literals": {
    "integer": { "decimal": "^-?[0-9]+$", ... },
    ...
  }
}
```

**Key sections:**
- `keywords` - Reserved words grouped by category
- `all_keywords` - Flat list of all reserved words
- `operators` - Operators grouped by type
- `operator_precedence` - Precedence levels (1=highest) with associativity
- `literals` - Regex patterns for literal validation
- `identifiers` - Identifier rules and patterns
- `comments` - Comment syntax
- `preprocessor` - Preprocessor directive patterns

### Parsing (grammar-rules.json)

Use for syntax validation - checking structure against grammar.

```json
{
  "declarations": {
    "class": {
      "pattern": "[modded] [sealed] class IDENTIFIER [: IDENTIFIER] { members }",
      "bnf": "classDecl ::= classModifier* 'class' IDENTIFIER ...",
      "modifiers_allowed": ["modded", "sealed"],
      "errors": { ... }
    },
    ...
  },
  "statements": {
    "if": {
      "pattern": "if ( expression ) statement [else statement]",
      "requires_parens": true,
      ...
    },
    ...
  }
}
```

**Key sections:**
- `declarations` - Class, enum, typedef, function, variable declarations
- `statements` - Control flow (if, for, while, switch, return, break, continue)
- `expressions` - Expression types (new, cast, call, member access, etc.)
- `attributes` - Attribute syntax and known attributes
- `modifiers` - All valid modifier keywords

### Type Checking (type-rules.json)

Use for type validation - checking type compatibility and conversions.

```json
{
  "primitive_types": {
    "int": { "size": 4, "default": 0, ... },
    ...
  },
  "reference_modifiers": {
    "ref": { "description": "Strong reference", "prevents_gc": true, ... },
    ...
  },
  "type_compatibility": {
    "implicit_conversions": [...],
    "explicit_cast_required": [...]
  },
  "operator_type_rules": {
    "arithmetic": { "valid_types": ["int", "float"], ... },
    ...
  }
}
```

**Key sections:**
- `primitive_types` - Built-in types with sizes and defaults
- `generic_types` - Parameterized types (array, set, map)
- `reference_modifiers` - ref, autoptr, weak, notnull semantics
- `type_compatibility` - Implicit/explicit conversion rules
- `operator_type_rules` - Which types support which operators

### Error Reporting (error-patterns.json)

Use for generating Workbench-compatible error messages.

```json
{
  "syntax_errors": [
    { "id": "E001", "pattern": "Identifier expected (character %d)", ... },
    ...
  ],
  "semantic_errors": [
    { "id": "E100", "pattern": "Unknown identifier '%.*s' (character %d)", ... },
    ...
  ],
  "warnings": [
    { "id": "W001", "pattern": "Variable '%s' is not used", ... },
    ...
  ]
}
```

**Error ID ranges:**
- `E001-E099` - Syntax errors
- `E100-E199` - Semantic errors (identifiers, functions, types)
- `W001-W099` - Warnings
- `has_position: true` - Error includes character position

**Severity levels:**
- `error` - Blocks compilation
- `warning` - Should fix but compiles
- `hint` - Code style suggestion

## Example: Validating Code

```pseudo
// 1. Tokenize
tokens = tokenize(source, tokens.json.keywords, tokens.json.operators)

// 2. Parse
ast = parse(tokens, grammar-rules.json.declarations, grammar-rules.json.statements)

// 3. Type check
errors = typecheck(ast, type-rules.json.type_compatibility)

// 4. Report
for error in errors:
    pattern = find_pattern(error-patterns.json, error.code)
    print(format(pattern, error.args))
```

## Integration

### AI Linter (Claude)

Load these JSON files into a system prompt for code review:

```
You are an Enforce Script linter. Use these rules to validate code:
- Keywords: [load tokens.json.keywords]
- Grammar: [load grammar-rules.json]
- Types: [load type-rules.json]
- Errors: [load error-patterns.json]
```

### CLI Validator

Build a parser that:
1. Loads `tokens.json` for lexer configuration
2. Loads `grammar-rules.json` for parser rules
3. Loads `type-rules.json` for type checker
4. Loads `error-patterns.json` for error formatting

## Source

Generated from `docs/reference/grammar.md` which was reverse-engineered from:
- Workbench binary error messages
- AST node types
- Parser regex patterns

## Version

- Schema version: 1.0.0
- Generated: 2024
- Source: docs/reference/grammar.md
