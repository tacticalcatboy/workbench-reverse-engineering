# Workbench NET API

TCP/IP interface for external tools to communicate with a running Workbench instance.

!!! warning "Limited External Use"
    The `ValidateScripts` endpoint appears to only work for internal Workbench files. Community members have reported issues getting external script validation working. A proper external validation API would need to be requested via the [BI Feedback Tracker](https://feedback.bistudio.com/).

## Overview

The NET API documentation describes:
1. **ValidateScripts** - Compile scripts and get errors (limited to internal use)
2. Check Workbench/compilation status
3. Open resources in Workbench
4. Create custom API endpoints

## Protocol

### Connection
- **Transport:** TCP/IP socket
- **Port:** Configurable in Workbench settings
- **Encoding:** UTF-8, little-endian integers

### Request Format

```
┌──────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Protocol Ver.│   Client ID     │   Content Type   │     Payload     │
│   (Integer)  │    (String)     │     (String)     │    (String)     │
└──────────────┴─────────────────┴──────────────────┴─────────────────┘
```

- **Protocol Ver:** `1` (only version supported)
- **Client ID:** Identifier like `"PythonClient"` or `"ClaudeAI"`
- **Content Type:** `"JsonRPC"`
- **Payload:** JSON object with `APIFunc` and parameters

### Response Format

```
┌──────────────┬─────────────────┐
│ Error Code   │     Payload     │
│   (String)   │    (String)     │
└──────────────┴─────────────────┘
```

## Built-in API Functions

### ValidateScripts (Most Important for AI)

Compiles scripts and returns structured errors/warnings.

**Request:**
```json
{
    "APIFunc": "ValidateScripts",
    "Configuration": "WORKBENCH"  // or "PC", "PLAYSTATION", "XBOX"
}
```

**Response:**
```json
{
    "Errors": [
        {
            "error": "Incompatible parameter 'b'",
            "file": "scripts/Game/game.c",
            "fileAbs": "F:\\DATA\\scripts\\Game\\game.c",
            "addon": "MyAddon",
            "line": 147
        }
    ],
    "Warnings": [
        {
            "error": "Variable 'a' is not used",
            "file": "scripts/Game/game.c",
            "fileAbs": "F:\\DATA\\scripts\\Game\\game.c",
            "addon": "MyAddon",
            "line": 146
        }
    ],
    "Success": false
}
```

### IsWorkbenchRunning

Check if Workbench is running and scripts are compiled.

**Request:**
```json
{
    "APIFunc": "IsWorkbenchRunning"
}
```

**Response:**
```json
{
    "IsRunning": true,
    "ScriptsCompiled": true
}
```

### IsWorldEditorRunning

Check if World Editor is running.

**Request:**
```json
{
    "APIFunc": "IsWorldEditorRunning"
}
```

**Response:**
```json
{
    "IsRunning": true,
    "ScriptsCompiled": true
}
```

### OpenResource

Open a resource file in Workbench.

**Request:**
```json
{
    "APIFunc": "OpenResource",
    "ResourceName": "scripts/Game/MyScript.c"
}
```

**Response:**
```json
{
    "Opened": true
}
```

### BringModuleWindowToFront

Bring a module window to front.

**Request:**
```json
{
    "APIFunc": "BringModuleWindowToFront",
    "ModuleName": "ScriptEditor"
}
```

## Custom API Endpoints

You can create custom handlers by implementing these classes:

### Request Class
```csharp
class MyRequest : JsonApiStruct
{
    string myParam;

    void MyRequest()
    {
        RegV("myParam");
    }
}
```

### Response Class
```csharp
class MyResponse : JsonApiStruct
{
    string result;

    void MyResponse()
    {
        RegV("result");
    }
}
```

### Handler Class
```csharp
class MyHandler : NetApiHandler
{
    override JsonApiStruct GetRequest()
    {
        return new MyRequest();
    }

    override JsonApiStruct GetResponse(JsonApiStruct request)
    {
        MyRequest req = MyRequest.Cast(request);
        MyResponse response = new MyResponse();

        // Process request
        response.result = "Processed: " + req.myParam;

        return response;
    }
}
```

## AI Coding Loop Architecture

```
┌─────────────┐     Write Code      ┌─────────────────┐
│   Claude    │────────────────────>│  Script Files   │
│    AI       │                     │   (.c files)    │
└─────────────┘                     └─────────────────┘
       ^                                     │
       │                                     │ Save
       │                                     v
       │ Structured               ┌─────────────────┐
       │ Errors/Warnings          │   Workbench     │
       │                          │  (NET API)      │
       └──────────────────────────│  ValidateScripts│
                                  └─────────────────┘
```

### Workflow

1. **AI writes code** to script files
2. **Call ValidateScripts** via NET API
3. **Parse JSON response** for errors/warnings
4. **AI fixes issues** based on structured feedback
5. **Repeat** until `Success: true`

## Python Client Example

```python
import socket
import struct
import json

def send_request(host, port, api_func, params=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # Build request
    protocol_ver = 1
    client_id = "PythonAI"
    content_type = "JsonRPC"

    payload = {"APIFunc": api_func}
    if params:
        payload.update(params)
    payload_json = json.dumps(payload)

    # Send: protocol version (int)
    sock.send(struct.pack('<I', protocol_ver))

    # Send: client ID (pascal string)
    client_bytes = client_id.encode('utf-8')
    sock.send(struct.pack('<I', len(client_bytes)))
    sock.send(client_bytes)

    # Send: content type (pascal string)
    content_bytes = content_type.encode('utf-8')
    sock.send(struct.pack('<I', len(content_bytes)))
    sock.send(content_bytes)

    # Send: payload (pascal string)
    payload_bytes = payload_json.encode('utf-8')
    sock.send(struct.pack('<I', len(payload_bytes)))
    sock.send(payload_bytes)

    # Receive response
    error_len = struct.unpack('<I', sock.recv(4))[0]
    error_code = sock.recv(error_len).decode('utf-8')

    response_len = struct.unpack('<I', sock.recv(4))[0]
    response_json = sock.recv(response_len).decode('utf-8')

    sock.close()
    return json.loads(response_json)

# Example: Validate scripts
result = send_request('localhost', 12345, 'ValidateScripts',
                      {'Configuration': 'WORKBENCH'})

if result['Success']:
    print("Scripts compiled successfully!")
else:
    for error in result['Errors']:
        print(f"ERROR {error['file']}:{error['line']}: {error['error']}")
    for warning in result['Warnings']:
        print(f"WARNING {warning['file']}:{warning['line']}: {warning['error']}")
```

## Configuration

The NET API port must be configured in Workbench settings. Check:
- Workbench > Settings > NET API
- Default port may vary

## Related Classes

- `NetApiHandler` - Base class for custom handlers
- `JsonApiStruct` - Base class for request/response objects
- `Workbench` - Main Workbench interface
