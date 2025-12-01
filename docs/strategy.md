# AI Tooling Strategy

Decision guide for AI-assisted Enforce Script development tooling.

## Project Vision

**Goal:** Create an external validation and debugging tool for Enforce Script that eliminates the need to open Workbench for day-to-day development.

### Development Workflow

```
Write Code → External Validator → Fix Errors → Repeat
                    ↓
              ┌───────────┐
              │ Our Tool  │  ← No Workbench needed!
              │ - Syntax  │
              │ - Types   │
              │ - API     │
              └───────────┘

Only for final upload → Workbench → BI Servers
```

## Project Goals

1. **Replace Workbench for validation** - Check syntax, types, and API usage externally
2. **Enable AI-assisted debugging** - Help AI understand and fix errors without Workbench
3. **Keep Workbench for upload only** - Still required for publishing mods to BI servers
4. **Create community tooling** - VS Code extension, CLI tools, CI/CD integration

## Current State

### Data Assets (Ready to Use)

| Asset | Location | Contents |
|-------|----------|----------|
| **Enfusion API** | `data/api/enfusion.json` | 824 classes, ~27K methods |
| **Arma Reforger API** | `data/api/arma-reforger.json` | 7,880 classes, ~202K methods |
| **Summary** | `data/api/summary.json` | Class names, method counts |
| **Inheritance Tree** | `data/api/inheritance-tree.json` | Class hierarchy |
| **Diagnostics** | `data/diagnostics/` | 270+ error patterns |

### What This Enables

- **Autocomplete** - All 8,704 class names, 229,617 method signatures
- **Type Checking** - Parameter types, return types from API data
- **Signature Validation** - Ensure method calls have correct arguments
- **Inheritance Checking** - Know what classes extend what

## Implementation Roadmap

### Phase 1: Data Foundation ✅ COMPLETE

- [x] Extract diagnostic patterns from binary (270+)
- [x] Discover official API docs (8,704 classes)
- [x] Parse API docs into structured JSON (229,617 methods)
- [x] Generate inheritance tree and summary

### Phase 2: API Surface Discovery ✅ COMPLETE

- [x] Study Enforce Script grammar in depth
- [x] Document attribute parameter rules
- [x] Map preprocessor directive support (#ifdef/#ifndef - no #define/#include)
- [x] Map class relationships (inheritance, composition, dependencies)
- [ ] Create syntax validation rules

### Phase 3: CLI Validator Tool

- [ ] Create Python/Node CLI tool
- [ ] Implement syntax checking (parse .c files)
- [ ] Implement API validation (check method calls against JSON)
- [ ] Implement type checking (parameter type validation)
- [ ] Generate error reports matching Workbench format

### Phase 4: Editor Integration

- [ ] VS Code extension with IntelliSense
- [ ] Real-time error highlighting
- [ ] Autocomplete from API data
- [ ] Go-to-definition support
- [ ] Hover documentation

### Phase 5: AI Integration

- [ ] MCP server for Claude Code integration
- [ ] Error explanation and fix suggestions
- [ ] Code generation with API awareness
- [ ] Automated testing support

## Technical Architecture

### CLI Validator Design

```
enforce-lint <file.c>
  │
  ├── Lexer/Tokenizer
  │     └── Tokenize Enforce Script syntax
  │
  ├── Parser
  │     └── Build AST from tokens
  │
  ├── API Validator
  │     ├── Load data/api/*.json
  │     ├── Check class names exist
  │     ├── Validate method signatures
  │     └── Check parameter types
  │
  ├── Type Checker
  │     ├── Infer variable types
  │     ├── Check assignments
  │     └── Validate returns
  │
  └── Reporter
        └── Output errors in Workbench-compatible format
```

## Strategic Advantages

### Why External Validation?

| Problem with Workbench | Our Solution |
|------------------------|--------------|
| Must open heavy GUI | Lightweight CLI tool |
| Can't integrate with CI/CD | Run in any pipeline |
| AI can't see Workbench errors | JSON error output for AI |
| No VS Code integration | Full LSP support |
| Slow iteration cycle | Instant validation |

### What Workbench Still Does

- **Mod upload** - Publishing to BI servers
- **Resource building** - Compiling assets
- **World editing** - 3D environment tools
- **Debugging runtime** - In-game debugging

We're not replacing these - just the code validation workflow.

## Research Findings

### Verified Data (100% Confidence)

| Source | Data |
|--------|------|
| Official docs | 8,704 class APIs with full signatures |
| Binary strings | 270+ diagnostic patterns |
| Binary strings | 1,833 ClassRegistrator entries |
| Binary strings | 373 RPC method names |

### Still Researching

| Topic | Status |
|-------|--------|
| Complete grammar rules | Needs analysis |
| Attribute parameters | Needs documentation |
| Preprocessor directives | Partially known |
| "Unused variable" detection | Unknown algorithm |
| "Can be const" hints | Unknown trigger |

## Available Prompts

| Prompt | Purpose |
|--------|---------|
| `prompts/grammar-analysis.md` | Study syntax rules |
| `prompts/attribute-rules.md` | Document attribute validation |
| `prompts/preprocessor-directives.md` | Map #ifdef support |
| `prompts/dll-analysis.md` | Explore DLL APIs |
| `prompts/class-relationships.md` | Map inheritance |

## Success Metrics

- [ ] Can validate a .c file without opening Workbench
- [ ] Catches 90%+ of errors Workbench would catch
- [ ] VS Code shows real-time errors
- [ ] AI can read validation output and fix code
- [ ] CI/CD pipeline integration working

## Legal Framework

See [Legal Analysis](legal.md) for details on:
- Interoperability exceptions
- Fair use analysis
- Community precedent (15+ years of Arma tools)
