# Syntax Validation Rules Generation

Convert the Enforce Script grammar documentation into machine-readable JSON rules for a linter/validator.

**Project Location:** C:\Users\scarlett\Documents\workbench-reverse-engineering

**Start by reading:**
1. `docs/reference/grammar.md` - Complete grammar documentation (BNF, keywords, operators)
2. `data/diagnostics/` - Error message patterns from Workbench
3. `data/api/summary.json` - API class/method counts for validation context

## Goal

Generate structured JSON files that a CLI linter can load to:
1. Tokenize Enforce Script source code
2. Validate syntax against grammar rules
3. Report errors in Workbench-compatible format

## Output Files

Create the following in `data/validation/`:

### 1. `tokens.json` - Lexical Rules

```json
{
  "keywords": {
    "control_flow": ["if", "else", "for", "foreach", "while", "switch", "case", "default", "break", "continue", "return"],
    "class_modifiers": ["class", "sealed", "modded", "abstract"],
    "access_modifiers": ["private", "protected", "public"],
    "member_modifiers": ["static", "native", "override", "const", "auto"],
    "reference_modifiers": ["ref", "autoptr", "weak", "notnull"],
    "parameter_modifiers": ["out", "inout"],
    "type_keywords": ["void", "typename", "enum", "typedef"],
    "special": ["new", "this", "super", "vanilla", "thread", "null", "NULL", "true", "false"]
  },
  "operators": {
    "arithmetic": ["+", "-", "*", "/", "%"],
    "comparison": ["==", "!=", "<", ">", "<=", ">="],
    "logical": ["&&", "||", "!"],
    "bitwise": ["&", "|", "^", "<<", ">>", "~"],
    "assignment": ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="],
    "unary": ["++", "--", "!", "-"],
    "ternary": ["?", ":"],
    "member": [".", "::"],
    "other": ["[", "]", "(", ")", "{", "}", ",", ";"]
  },
  "operator_precedence": [
    {"level": 1, "operators": ["()", "[]", "."], "associativity": "left"},
    {"level": 2, "operators": ["++", "--"], "associativity": "left", "note": "postfix"},
    {"level": 3, "operators": ["!", "-", "++", "--"], "associativity": "right", "note": "unary/prefix"},
    {"level": 4, "operators": ["new", "(type)"], "associativity": "right"},
    {"level": 5, "operators": ["*", "/", "%"], "associativity": "left"},
    {"level": 6, "operators": ["+", "-"], "associativity": "left"},
    {"level": 7, "operators": ["<<", ">>"], "associativity": "left"},
    {"level": 8, "operators": ["<", "<=", ">", ">="], "associativity": "left"},
    {"level": 9, "operators": ["==", "!="], "associativity": "left"},
    {"level": 10, "operators": ["&"], "associativity": "left"},
    {"level": 11, "operators": ["^"], "associativity": "left"},
    {"level": 12, "operators": ["|"], "associativity": "left"},
    {"level": 13, "operators": ["&&"], "associativity": "left"},
    {"level": 14, "operators": ["||"], "associativity": "left"},
    {"level": 15, "operators": ["?:"], "associativity": "right"},
    {"level": 16, "operators": ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="], "associativity": "right"}
  ],
  "literals": {
    "integer": {
      "decimal": "^-?[0-9]+$",
      "hex": "^0[xX][0-9a-fA-F]+$",
      "binary": "^0[bB][01]+$"
    },
    "float": "^-?[0-9]*\\.[0-9]+([eE][+-]?[0-9]+)?[fF]?$",
    "string": "^\"([^\"\\\\]|\\\\.)*\"$",
    "boolean": ["true", "false"],
    "null": ["null", "NULL"]
  },
  "identifiers": {
    "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$",
    "reserved": "<<all keywords above>>"
  },
  "comments": {
    "single_line": "//",
    "multi_line_start": "/*",
    "multi_line_end": "*/"
  },
  "preprocessor": {
    "directives": ["#ifdef", "#ifndef", "#if", "#else", "#endif", "#define", "#include"],
    "pattern": "^#[a-zA-Z]+"
  }
}
```

### 2. `grammar-rules.json` - Syntax Rules

```json
{
  "declarations": {
    "class": {
      "pattern": "[modded] [sealed] class IDENTIFIER [: IDENTIFIER] { members }",
      "modifiers_allowed": ["modded", "sealed"],
      "requires_body": true,
      "inheritance": {
        "keyword": ":",
        "single_only": true
      },
      "errors": {
        "sealed_inheritance": "'%s': cannot derive from sealed type '%s'",
        "sealed_modded": "Sealed type '%s' can't be modded",
        "circular": "Circular class inheritance"
      }
    },
    "enum": {
      "pattern": "enum IDENTIFIER { values }",
      "value_pattern": "IDENTIFIER [= expression]",
      "separator": ",",
      "errors": {
        "complex_value": "Only simple expressions supported in enum value '%s'"
      }
    },
    "typedef": {
      "pattern": "typedef TYPE IDENTIFIER ;",
      "errors": {
        "circular": "Circle inheritance in typedef '%s'"
      }
    },
    "function": {
      "pattern": "[modifiers] TYPE IDENTIFIER ( [params] ) [override] { body }",
      "modifiers_allowed": ["static", "native", "private", "protected", "override", "sealed"],
      "errors": {
        "override_missing": "Overriding function '%s' but not marked as 'override'",
        "override_no_base": "Function '%s' is marked as override, but there is no function with this name in the base class",
        "static_mismatch": "Function '%s' override signature conflict: differing 'static' usage",
        "no_return": "No return statement in function returning non-void '%s'",
        "void_return": "return-statement with a value, in function returning 'void'"
      }
    },
    "variable": {
      "pattern": "[modifiers] TYPE IDENTIFIER [= expression] ;",
      "modifiers_allowed": ["static", "const", "auto", "ref", "autoptr", "weak", "notnull", "private", "protected"],
      "errors": {
        "static_auto": "static/const variables can't be auto",
        "can_be_const": "Variable '%s' can be const",
        "unused": "Variable '%s' is not used",
        "missing_ref": "Variable '%s' is not strong ref (missing 'ref' keyword?)"
      }
    },
    "parameter": {
      "pattern": "[modifiers] TYPE IDENTIFIER [= default]",
      "modifiers_allowed": ["out", "inout", "notnull"],
      "errors": {
        "native_out": "Native functions don't support 'out' arguments '%s'",
        "wrong_context": "inout/out/notnull can be used only on function parameters"
      }
    }
  },
  "statements": {
    "if": {
      "pattern": "if ( expression ) statement [else statement]",
      "requires_parens": true,
      "requires_condition": true,
      "errors": {
        "always_true": "If statement condition always true",
        "always_false": "If statement condition always false",
        "no_args": "If statement without arguments."
      }
    },
    "for": {
      "pattern": "for ( [init] ; [condition] ; [update] ) statement",
      "requires_parens": true,
      "semicolons_required": 2
    },
    "foreach": {
      "pattern": "foreach ( TYPE IDENTIFIER : expression ) statement",
      "requires_parens": true,
      "separator": ":"
    },
    "while": {
      "pattern": "while ( expression ) statement",
      "requires_parens": true,
      "requires_condition": true
    },
    "switch": {
      "pattern": "switch ( expression ) { cases }",
      "requires_parens": true,
      "requires_braces": true,
      "case_pattern": "case expression : statements",
      "default_pattern": "default : statements",
      "errors": {
        "fallthrough": "Switch: fall through cases can't have a body"
      }
    },
    "return": {
      "pattern": "return [expression] ;",
      "requires_semicolon": true
    },
    "break": {
      "pattern": "break ;",
      "requires_semicolon": true,
      "valid_contexts": ["for", "foreach", "while", "switch"],
      "errors": {
        "misplaced": "Misplaced break/case/continue"
      }
    },
    "continue": {
      "pattern": "continue ;",
      "requires_semicolon": true,
      "valid_contexts": ["for", "foreach", "while"],
      "errors": {
        "misplaced": "Misplaced break/case/continue"
      }
    },
    "expression": {
      "pattern": "expression ;",
      "requires_semicolon": true,
      "errors": {
        "missing_semicolon": "Broken expression (missing ';'?)"
      }
    }
  },
  "expressions": {
    "new": {
      "pattern": "new TYPE [( [args] )]",
      "errors": {
        "private_constructor": "Can't clone class '%s', constructor is not public"
      }
    },
    "cast": {
      "patterns": ["( TYPE ) expression", "TYPE.Cast( expression )"],
      "errors": {
        "excessive": "Excessive cast, variable '%s' already has type '%s'"
      }
    },
    "call": {
      "pattern": "expression ( [args] )",
      "errors": {
        "not_enough_params": "Not enough parameters in function '%s'",
        "wrong_count": "Wrong argument count for function '%.*s' (character %d)",
        "wrong_types": "Wrong argument types for function '%.*s' (character %d)"
      }
    },
    "member_access": {
      "pattern": "expression . IDENTIFIER"
    },
    "array_access": {
      "pattern": "expression [ expression ]"
    },
    "ternary": {
      "pattern": "expression ? expression : expression"
    },
    "this_super": {
      "keywords": ["this", "super"],
      "errors": {
        "in_static": "'this' or 'super' inside static method is not valid"
      }
    }
  },
  "attributes": {
    "pattern": "[ IDENTIFIER [( [args] )] ]",
    "placement": ["before_class", "before_function", "before_field"],
    "arg_patterns": ["expression", "IDENTIFIER = expression"],
    "known_attributes": {
      "Attribute": {"params": ["defvalue", "desc", "uiwidget", "enums", "params", "category"]},
      "RplRpc": {"params": ["channel", "receiver"]},
      "RplProp": {"params": ["onRplName", "condition"]},
      "BaseContainerProps": {"params": []},
      "ComponentEditorProps": {"params": ["category", "description"]}
    }
  }
}
```

### 3. `type-rules.json` - Type System Rules

```json
{
  "primitive_types": {
    "void": {"size": 0, "assignable": false},
    "int": {"size": 4, "default": 0, "literals": ["integer"]},
    "float": {"size": 4, "default": 0.0, "literals": ["float", "integer"]},
    "bool": {"size": 1, "default": false, "literals": ["boolean"]},
    "string": {"size": "variable", "default": "\"\"", "literals": ["string"]},
    "vector": {"size": 12, "default": "\"0 0 0\"", "components": ["x", "y", "z"]}
  },
  "generic_types": {
    "array": {"syntax": "array<T>", "type_params": 1},
    "set": {"syntax": "set<T>", "type_params": 1},
    "map": {"syntax": "map<K,V>", "type_params": 2}
  },
  "reference_modifiers": {
    "ref": {
      "description": "Strong reference",
      "prevents_gc": true,
      "valid_for": ["class_types"]
    },
    "autoptr": {
      "description": "Auto-releasing pointer",
      "auto_cleanup": true,
      "valid_for": ["class_types"],
      "errors": {
        "non_managed": "autoptr/ref in template is not supported on non-managed class '%s'"
      }
    },
    "weak": {
      "description": "Weak reference",
      "prevents_gc": false,
      "valid_for": ["class_types"],
      "errors": {
        "should_use_ref": "Script variable '%s.%s': using weak pointer to store object, use 'ref' for strong reference"
      }
    },
    "notnull": {
      "description": "Non-null constraint",
      "compile_time_check": true,
      "valid_for": ["class_types", "parameters"],
      "errors": {
        "invalid_type": "'notnull' must not be used with '%s' type"
      }
    }
  },
  "type_compatibility": {
    "implicit_conversions": [
      {"from": "int", "to": "float"},
      {"from": "int", "to": "bool"},
      {"from": "float", "to": "bool"},
      {"from": "derived_class", "to": "base_class"}
    ],
    "explicit_cast_required": [
      {"from": "float", "to": "int"},
      {"from": "base_class", "to": "derived_class"}
    ]
  },
  "operator_type_rules": {
    "arithmetic": {
      "valid_types": ["int", "float", "vector"],
      "result_type": "promote_to_float_if_mixed"
    },
    "comparison": {
      "valid_types": ["int", "float", "bool", "string"],
      "result_type": "bool"
    },
    "logical": {
      "valid_types": ["bool"],
      "result_type": "bool",
      "errors": {
        "invalid": "'%s' not supported on 'bool'"
      }
    },
    "bitwise": {
      "valid_types": ["int"],
      "result_type": "int"
    }
  }
}
```

### 4. `error-patterns.json` - Diagnostic Patterns

```json
{
  "syntax_errors": [
    {
      "id": "E001",
      "pattern": "Identifier expected (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E002",
      "pattern": "Expression expected (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E003",
      "pattern": "String expected (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E004",
      "pattern": "Number expected (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E005",
      "pattern": "Unexpected symbol '%.*s' (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E006",
      "pattern": "Unmatched parenthesis '%.*s' (character %d)",
      "severity": "error",
      "category": "syntax",
      "has_position": true
    },
    {
      "id": "E007",
      "pattern": "CParser: quoted string not closed on line %d, module %s",
      "severity": "error",
      "category": "syntax"
    },
    {
      "id": "E008",
      "pattern": "Expected name, not a keyword '%s'",
      "severity": "error",
      "category": "syntax"
    },
    {
      "id": "E009",
      "pattern": "Broken expression (missing ';'?)",
      "severity": "error",
      "category": "syntax"
    }
  ],
  "semantic_errors": [
    {
      "id": "E100",
      "pattern": "Unknown identifier '%.*s' (character %d)",
      "severity": "error",
      "category": "semantic"
    },
    {
      "id": "E101",
      "pattern": "Cannot convert '%s' to '%s'",
      "severity": "error",
      "category": "type"
    },
    {
      "id": "E102",
      "pattern": "Not enough parameters in function '%s'",
      "severity": "error",
      "category": "semantic"
    },
    {
      "id": "E103",
      "pattern": "method '%s' has wrong return type, expected '%s' actual '%s'",
      "severity": "error",
      "category": "type"
    },
    {
      "id": "E104",
      "pattern": "method '%s' is private",
      "severity": "error",
      "category": "access"
    },
    {
      "id": "E105",
      "pattern": "class '%s' cannot extend sealed class '%s'",
      "severity": "error",
      "category": "inheritance"
    },
    {
      "id": "E106",
      "pattern": "method '%s' cannot override sealed method",
      "severity": "error",
      "category": "inheritance"
    },
    {
      "id": "E107",
      "pattern": "Overriding function '%s' but not marked as 'override'",
      "severity": "error",
      "category": "inheritance"
    }
  ],
  "warnings": [
    {
      "id": "W001",
      "pattern": "Variable '%s' is not used",
      "severity": "warning",
      "category": "unused"
    },
    {
      "id": "W002",
      "pattern": "Variable '%s' can be const",
      "severity": "hint",
      "category": "style"
    },
    {
      "id": "W003",
      "pattern": "Excessive cast, variable '%s' already has type '%s'",
      "severity": "warning",
      "category": "redundant"
    },
    {
      "id": "W004",
      "pattern": "If statement condition always true",
      "severity": "warning",
      "category": "logic"
    },
    {
      "id": "W005",
      "pattern": "If statement condition always false",
      "severity": "warning",
      "category": "logic"
    },
    {
      "id": "W006",
      "pattern": "Forward declarations are deprecated",
      "severity": "warning",
      "category": "deprecated"
    }
  ],
  "severity_levels": {
    "error": {"exit_code": 1, "blocks_compilation": true},
    "warning": {"exit_code": 0, "blocks_compilation": false},
    "hint": {"exit_code": 0, "blocks_compilation": false}
  }
}
```

## Tasks

### Task 1: Extract Token Rules
From grammar.md, extract all tokens into `tokens.json`:
- All keywords (grouped by category)
- All operators (with precedence)
- Literal patterns (regex for validation)
- Identifier rules
- Comment syntax

### Task 2: Generate Grammar Rules
Convert the BNF grammar (lines 706-792 of grammar.md) into `grammar-rules.json`:
- Declaration patterns
- Statement patterns
- Expression patterns
- Attribute patterns
- Include error messages for each rule

### Task 3: Define Type Rules
Create `type-rules.json` covering:
- Primitive types with defaults
- Generic type syntax
- Reference modifier rules
- Type compatibility/conversion rules
- Operator type requirements

### Task 4: Compile Error Patterns
From grammar.md error references and `data/diagnostics/`, create `error-patterns.json`:
- Assign unique IDs to each error
- Categorize by type (syntax, semantic, type, etc.)
- Include severity levels
- Note which have position information

### Task 5: Validate Completeness
Cross-check the generated JSON against:
- All error messages in grammar.md
- All keywords mentioned
- All operators listed
- BNF grammar rules

## Output Structure

```
data/
└── validation/
    ├── tokens.json          # Lexical rules
    ├── grammar-rules.json   # Syntax rules
    ├── type-rules.json      # Type system rules
    ├── error-patterns.json  # Diagnostic patterns
    └── README.md            # Schema documentation
```

## Validation Criteria

The generated JSON should enable:
1. **Tokenization** - Split source into tokens using `tokens.json`
2. **Parsing** - Validate structure using `grammar-rules.json`
3. **Type checking** - Validate types using `type-rules.json`
4. **Error reporting** - Match Workbench output using `error-patterns.json`

## When Complete

1. Create `data/validation/` directory with all JSON files
2. Create `data/validation/README.md` documenting the schema
3. Update `docs/strategy.md`:
   - Mark "Create syntax validation rules" as complete
   - Phase 2 is now COMPLETE
4. Update `docs/reference/grammar.md` to reference the JSON files

## Notes

- Keep JSON files human-readable (formatted with indentation)
- Use consistent naming conventions (snake_case for keys)
- Include comments where JSON5 is acceptable, otherwise use `_comment` fields
- Regex patterns should be escaped for JSON strings
