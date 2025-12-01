# Workbench Reverse Engineering Project

Reverse-engineering Arma Reforger Workbench to document **Enforce Script** - a C-like scripting language for game modding.

## Key Directories

```
docs/                    # MkDocs documentation (mkdocs serve to view)
  findings/              # Discovered patterns and keywords
  reference/             # Grammar, AST, compiler docs
data/workbench/          # Extracted strings from binaries
  all_strings.txt        # 84,718 strings - primary analysis source
```

## Enforce Script Quick Facts

- C-like syntax with classes, enums, functions
- Reference modifiers: `ref`, `autoptr`, `weak`, `notnull`
- `modded` keyword for class extension (modding system)
- `vanilla` keyword to access original class in modded classes
- Square bracket attributes: `[Attribute(params)]`
- No exceptions (no try/catch)

## When Creating New Doc Files

Always update `mkdocs.yml` nav section to include the new file.

## Evidence-Based Documentation

All findings should include evidence from error messages, AST nodes, or parser messages found in the extracted strings.
