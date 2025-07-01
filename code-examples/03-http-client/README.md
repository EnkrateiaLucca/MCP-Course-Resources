# MCP HTTP Client Example

This example demonstrates how to build a client that connects to MCP servers using HTTP transport.

## Features

- Connects to MCP servers via streamable HTTP
- Integrates with Claude API for natural language processing
- Interactive chat interface
- Dynamic tool discovery and execution

## Setup

1. Install dependencies:
```bash
pip install mcp anthropic httpx python-dotenv
```

2. Set up environment variables:
```bash
export ANTHROPIC_API_KEY="your-api-key"
```

3. Run the client:
```bash
python client_streamable_http.py --server-url http://localhost:8000
```

## Usage

The client provides an interactive chat interface where you can:
- Type natural language commands
- The client will use Claude to understand your intent
- Automatically call appropriate MCP tools
- Display results in the conversation

Type 'quit' or 'exit' to end the session.

## Architecture

- Uses async/await for concurrent operations
- Manages MCP session lifecycle
- Handles tool discovery and execution
- Maintains conversation context between Claude and MCP tools