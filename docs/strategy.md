# AI Tooling Strategy

Decision guide for AI-assisted Enforce Script development tooling.

## Project Vision

**Goal:** Create an external validation and debugging tool for Enforce Script that eliminates the need to open Workbench for day-to-day development.

### Development Workflow

```
Write Code → External Validator → Fix Errors → Repeat
                    ↓
         ┌─────────────────────────────────────┐
         │            TWO OPTIONS              │
         ├──────────────┬──────────────────────┤
         │ AI Linter    │  CLI Validator       │
         │ (Prompt)     │  (Program)           │
         ├──────────────┼──────────────────────┤
         │ • Claude     │  • Python/Node       │
         │ • Flexible   │  • Deterministic     │
         │ • Explains   │  • CI/CD ready       │
         │ • Quick win  │  • Fast on large     │
         └──────────────┴──────────────────────┘

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
- [x] Create syntax validation rules (JSON for linter) - see `data/validation/`

### Phase 3a: AI Linter Prompt ✅ COMPLETE

- [x] Generate `data/validation/*.json` from grammar.md
- [x] Create linter system prompt referencing JSON rules (updated `docs/prompts/linter/`)
- [x] Create CLAUDE.md snippet for project integration (`docs/prompts/linter/claude-md-snippet.md`)
- [x] Test against real Enforce Script code (Overthrow) - Found 6 errors, 2 warnings
- [x] Document usage in `docs/tools/linter.md`

**What it is:** A Claude prompt that uses JSON validation rules to review code.
**Advantage:** Works immediately, explains errors, suggests fixes.

### Phase 3b: CLI Validator Tool ✅ CORE COMPLETE

- [x] Create Python CLI tool (`tools/enforce-lint/`)
- [x] Implement lexer/tokenizer (`src/lexer.py`)
- [x] Implement AST node classes (`src/ast_nodes.py`)
- [x] Implement recursive descent parser (`src/parser.py`)
- [x] Implement AST-based semantic analyzer (`validators/ast_validator.py`)
- [x] Generate error reports matching Workbench format
- [ ] Implement full API validation (check method calls against JSON)
- [ ] Implement comprehensive type checking (parameter type validation)

**What it is:** A standalone program that parses and validates code.
**Advantage:** Deterministic, fast, CI/CD integration, no AI needed.

**Components Built:**
- Full lexer with support for all Enforce Script tokens
- Complete AST node hierarchy for all language constructs
- Recursive descent parser implementing the full grammar
- Semantic analyzer detecting:
  - Misplaced break/continue statements
  - Return type violations
  - Static context violations (this/super in static)
  - Missing return statements
  - Override keyword warnings

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

### AI Linter Design (Phase 3a)

```
┌─────────────────────────────────────────────────────────┐
│                    AI LINTER PROMPT                     │
├─────────────────────────────────────────────────────────┤
│ System Prompt:                                          │
│   "You are an Enforce Script linter..."                 │
│                                                         │
│ Knowledge Base (JSON files):                            │
│   ├── data/validation/tokens.json                       │
│   ├── data/validation/grammar-rules.json                │
│   ├── data/validation/type-rules.json                   │
│   ├── data/validation/error-patterns.json               │
│   └── data/api/*.json (class/method signatures)         │
│                                                         │
│ Input: User pastes code or references file              │
│ Output: Errors, warnings, hints with explanations       │
└─────────────────────────────────────────────────────────┘
```

**Usage:** Add linter prompt to CLAUDE.md or use as standalone prompt.

### CLI Validator Design (Phase 3b)

```
enforce-lint <file.c>
  │
  ├── Lexer/Tokenizer
  │     └── Tokenize using data/validation/tokens.json
  │
  ├── Parser
  │     └── Build AST using data/validation/grammar-rules.json
  │
  ├── API Validator
  │     ├── Load data/api/*.json
  │     ├── Check class names exist
  │     ├── Validate method signatures
  │     └── Check parameter types
  │
  ├── Type Checker
  │     ├── Load data/validation/type-rules.json
  │     ├── Infer variable types
  │     ├── Check assignments
  │     └── Validate returns
  │
  └── Reporter
        ├── Load data/validation/error-patterns.json
        └── Output errors in Workbench-compatible format
```

**Usage:** `enforce-lint src/**/*.c` or integrate into CI/CD pipeline.

## Strategic Advantages

### AI Linter vs CLI Validator

| Aspect | AI Linter (Prompt) | CLI Validator (Program) |
|--------|-------------------|------------------------|
| **Speed to implement** | Fast (just a prompt) | Slow (full parser) |
| **Accuracy** | Good (AI reasoning) | Exact (deterministic) |
| **Explanations** | Rich (explains why) | Basic (error codes) |
| **CI/CD** | No | Yes |
| **Large codebases** | Slow/expensive | Fast |
| **Offline** | No (needs API) | Yes |
| **Fix suggestions** | Yes (AI generates) | No (just reports) |

**Recommendation:** Start with AI Linter for quick wins, build CLI Validator for automation.

### Why External Validation?

| Problem with Workbench | Our Solution |
|------------------------|--------------|
| Must open heavy GUI | Lightweight CLI tool or AI prompt |
| Can't integrate with CI/CD | CLI validator in any pipeline |
| AI can't see Workbench errors | JSON error output for AI |
| No VS Code integration | Full LSP support (Phase 4) |
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

| Prompt | Purpose | Phase |
|--------|---------|-------|
| `prompts/grammar-analysis.md` | Study syntax rules | 2 |
| `prompts/attribute-rules.md` | Document attribute validation | 2 |
| `prompts/preprocessor-directives.md` | Map #ifdef support | 2 |
| `prompts/dll-analysis.md` | Explore DLL APIs | 1 |
| `prompts/class-relationships.md` | Map inheritance | 2 |
| `prompts/syntax-validation-rules.md` | Convert grammar to JSON for linter | 2 |
| `prompts/enforce-linter.md` | AI linter system prompt (TBD) | 3a |

## Success Metrics

### Phase 3a (AI Linter)
- [x] AI linter prompt catches common errors (missing override, null checks, type mismatches)
- [x] Can review a .c file without opening Workbench
- [x] AI explains errors and suggests fixes
- [ ] Integrated into Overthrow CLAUDE.md for testing

### Phase 3b (CLI Validator)
- [x] CLI tool parses valid Enforce Script without errors
- [ ] Catches 90%+ of errors Workbench would catch (partial - semantic errors working)
- [ ] CI/CD pipeline integration working (ready - JSON output supported)
- [x] Output matches Workbench error format

### Phase 4+ (Editor/AI)
- [ ] VS Code shows real-time errors
- [ ] AI can read validation output and fix code automatically

## Legal Framework

See [Legal Analysis](legal.md) for details on:
- Interoperability exceptions
- Fair use analysis
- Community precedent (15+ years of Arma tools)
