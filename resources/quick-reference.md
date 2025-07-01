# MCP Quick Reference Guide

## Core Concepts

### Components
- **Host**: The application running MCP (Claude, Cursor, VS Code)
- **Client**: Manages connections between host and servers
- **Server**: Exposes tools, resources, and prompts

### Capabilities
- **Tools**: Functions AI can call
- **Resources**: Data AI can access
- **Prompts**: Pre-configured conversations
- **Sampling**: Text generation capabilities

## Basic Server Template

```python
from mcp import FastMCP

# Create server
mcp = FastMCP("server-name")

# Define a tool
@mcp.tool()
def my_tool(param: str) -> dict:
    """Tool description"""
    return {"result": param}

# Run server
if __name__ == "__main__":
    mcp.run()
```

## Transport Options

### STDIO (Default)
```python
mcp.run()  # Uses stdin/stdout
```

### HTTP with SSE
```python
mcp = FastMCP("server", stateless_http=True)
mcp.run(transport="http", port=8000)
```

## Common Patterns

### Error Handling
```python
@mcp.tool()
def safe_tool(path: str) -> dict:
    try:
        # Tool logic
        return {"success": True, "data": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

### Resource with Dynamic Content
```python
@mcp.resource("data://current-time")
def get_time() -> str:
    return datetime.now().isoformat()
```

### Prompt with Context
```python
@mcp.prompt()
def analyze_code() -> list:
    return [
        {"role": "system", "content": "You are a code analyzer"},
        {"role": "user", "content": "Analyze the provided code"}
    ]
```

## Configuration Examples

### Claude Code (stdio)
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

### Cursor (stdio)
```json
{
  "mcp": {
    "servers": {
      "my-server": {
        "command": "python",
        "args": ["server.py"],
        "cwd": "/path/to/project"
      }
    }
  }
}
```

## Debugging Tips

1. **Enable logging**:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Test with client**:
   ```python
   python -m mcp.client stdio python server.py
   ```

3. **Check server health**:
   ```bash
   curl http://localhost:8000/health
   ```

## Common Issues

### Server not found
- Check file path in configuration
- Ensure Python is in PATH
- Verify file permissions

### Tool not working
- Check parameter types match
- Ensure return value is JSON-serializable
- Add logging to debug

### Connection issues
- Verify transport settings
- Check firewall/port availability
- Test with simple client first

## Best Practices

1. **Keep tools focused**: One clear purpose per tool
2. **Use descriptive names**: Tools should be self-explanatory
3. **Handle errors gracefully**: Always return structured responses
4. **Document thoroughly**: Clear docstrings help AI use tools correctly
5. **Test independently**: Test servers before integration

## Useful Commands

```bash
# Install MCP
pip install mcp[cli]

# Run server directly
python server.py

# Test with MCP client
python -m mcp.client stdio python server.py

# List available tools
python -c "from server import mcp; print([t.name for t in mcp.list_tools()])"
```

## Links

- [MCP Specification](https://spec.modelcontextprotocol.io)
- [Python SDK Docs](https://github.com/modelcontextprotocol/python-sdk)
- [Example Servers](https://github.com/modelcontextprotocol/examples)
- [Community Forum](https://github.com/modelcontextprotocol/protocol/discussions)