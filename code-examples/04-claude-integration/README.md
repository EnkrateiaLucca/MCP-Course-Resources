# Claude Desktop MCP Server Example

This is a minimal MCP server designed for integration with Claude Desktop.

## Features

- Ultra-simple implementation (13 lines)
- Single demonstration tool
- Designed for Claude Desktop configuration testing

## Setup

1. Install dependencies:
```bash
pip install mcp[cli]
```

2. Configure in Claude Desktop:
   - Add server configuration to Claude Desktop settings
   - Point to the Python executable and this script

3. Run the server:
```bash
python claude_mcp_server.py
```

## Usage

Once configured in Claude Desktop, the server's tools will be available to Claude during conversations.

## Configuration Example

Add to Claude Desktop configuration:
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/path/to/claude_mcp_server.py"]
    }
  }
}
```