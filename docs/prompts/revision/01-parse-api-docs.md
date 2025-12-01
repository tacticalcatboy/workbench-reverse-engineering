# 01 - Parse Official API Docs to JSON

Parse the Doxygen HTML documentation into structured JSON for AI consumption.

## Context

- **Input:** Doxygen HTML files at `D:\SteamLibrary\steamapps\common\Arma Reforger Tools\Workbench\docs\`
- **Output:** Structured JSON files in `data/api/`
- **Purpose:** Create machine-readable API data for AI linting and autocomplete

## Data Sources

| API | Location | Classes |
|-----|----------|---------|
| EnfusionScriptAPIPublic | `Workbench\docs\EnfusionScriptAPIPublic\` | 824 |
| ArmaReforgerScriptAPIPublic | `Workbench\docs\ArmaReforgerScriptAPIPublic\` | 7,880 |

## Task

### Step 1: Analyze HTML Structure

Read sample class files to understand the Doxygen HTML structure:
- Class name and inheritance
- Method signatures (return type, name, parameters)
- Properties/fields
- Documentation comments

### Step 2: Create Parser Script

Create a Python script at `scripts/parse_api_docs.py` that:

1. Recursively finds all `class*.html` files
2. Extracts for each class:
   ```json
   {
     "name": "ClassName",
     "extends": "ParentClass",
     "module": "Game",
     "methods": [
       {
         "name": "MethodName",
         "returnType": "void",
         "parameters": [
           {"name": "param1", "type": "int"},
           {"name": "param2", "type": "string"}
         ],
         "static": false,
         "access": "public"
       }
     ],
     "properties": [
       {"name": "fieldName", "type": "float", "access": "protected"}
     ]
   }
   ```
3. Outputs to `data/api/enfusion.json` and `data/api/arma-reforger.json`

### Step 3: Generate Summary

Create `data/api/summary.json` with:
- Total class count
- Class names list (for quick autocomplete)
- Method count per class
- Inheritance tree

## Expected Output Structure

```
data/
├── api/
│   ├── enfusion.json           # 824 classes
│   ├── arma-reforger.json      # 7,880 classes
│   ├── summary.json            # Quick lookup data
│   └── inheritance-tree.json   # Class hierarchy
```

## Validation

After completion:
1. Verify class count matches expected (824 + 7,880 = 8,704)
2. Spot-check 5 random classes against HTML source
3. Ensure all methods have valid type information

## Dependencies

- Python 3.x
- BeautifulSoup4 (`pip install beautifulsoup4`)
- lxml (`pip install lxml`)

## Next Prompt

After completing this task, proceed to `02-create-cli-tool.md`
