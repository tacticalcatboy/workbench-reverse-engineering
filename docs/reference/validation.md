# Validation System

Components that validate Enforce Script code.

## Core Components

| Component | Namespace | Purpose |
|-----------|-----------|---------|
| `EScriptValidationResult` | - | Validation result enum |
| `EntityValidationBase` | `enf` | Base validation class |
| `EntityValidationCollection` | `enf` | Collection of validations |
| `CParseErrorHandler` | `enf` | Parse error handler |
| `FirstErrorHandler` | `ScriptProject@enf` | First error handler |
| `ValidateScripts` | `NetApiNative` | Script validation API |

## Entity Validators

| Validator | Namespace | Purpose |
|-----------|-----------|---------|
| `EntityDataValidation` | `gamelib` | Entity data validation |
| `EntitySkewValidation` | `gamelib` | Entity skew/transform validation |
| `WorldBoundsValidation` | `gamelib` | World boundary validation |
| `WaterBodyValidation` | `gamelib` | Water body validation |

## Validation Errors

### Required Attributes

| Pattern | Meaning |
|---------|---------|
| `%s: The attribute '%s' is required but missing.` | Required attribute not provided |
| `%sThe attribute '%s' is not allowed.` | Attribute not valid in context |

### Content Validation

| Pattern | Meaning |
|---------|---------|
| `%s: The content is not valid. Expected is %s.` | Invalid content type |
| `%s: The facet '%s' is not allowed on types derived from the type %s.` | Facet restriction violation |
| `%s: The facet '%s' is not allowed.` | Invalid facet |

## Trigger Conditions

Common patterns that trigger validation errors:

| Pattern | Meaning |
|---------|---------|
| `must be` | Required condition |
| `should be` | Recommended condition |
| `is required` | Mandatory requirement |
| `cannot` | Prohibited action |
| `not supported` | Unsupported operation |
| `is missing` | Missing dependency |

## Attribute Validation

### Parameter Validation

| Error | Cause |
|-------|-------|
| `Attribute %s doesn't have parameter %s set up` | Missing required parameter |
| `Attribute %s not in 'Variables' category` | Wrong category |
| `Attribute %s has invalid type %s in it's parameters` | Invalid parameter type |

### Method Validation (for attributes)

| Error | Cause |
|-------|-------|
| `'%s' method... doesn't exist` | Referenced method missing |
| `...should have only 1 parameter` | Wrong parameter count |
| `...should not return any value` | Should be void |
| `...parameter type... is not equal to the variable type` | Type mismatch |

## Custom Condition Methods

Validation for custom condition methods:

| Error | Cause |
|-------|-------|
| `Custom condition method '%s.%s' has wrong number of parameters. Expected 0, found %u.` | Too many parameters |
| `Custom condition method '%s.%s' has wrong number of parameters. Expected 1, found %u.` | Wrong parameter count |
| `Custom condition method '%s.%s' has wrong parameter type. Expected '%s', found '%s'.` | Wrong parameter type |
| `Custom condition method '%s.%s' has wrong return type. Expected '%s', found '%s'.` | Wrong return type |

## Configuration Files

| File | Purpose |
|------|---------|
| `validation.conf` | Validation settings |

## Diagnostic Menu

| Component | Purpose |
|-----------|---------|
| `DiagMenuAPIRegistrator` | Diagnostic menu registration |
| `DiagMenuWidget` | Menu UI widget |
| `EDiagMenuGame` | Game menu enum |
| `EDiagMenuGameLib` | GameLib menu enum |
| `diagmenu.save` | Persisted menu state |
