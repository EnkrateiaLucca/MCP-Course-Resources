# Code Documentation Assistant - MCP Tutorial

Build a practical Model Context Protocol (MCP) server that helps developers automatically generate documentation for their code. This tutorial will walk you through creating an MCP server using HTTP/SSE transport that exposes tools for code analysis and documentation generation.

## 🎯 What We'll Build

A Code Documentation Assistant that can:
- Analyze Python files and extract their structure (classes, functions, docstrings)
- Generate documentation for specific functions
- Create README files for projects
- Extract TODO/FIXME comments from codebases
- Provide documentation templates

This is a perfect example for learning MCP because it's:
- **Simple**: Easy to understand and implement
- **Practical**: Actually useful for developers
- **Extensible**: Can be enhanced with more features

## 📋 Prerequisites

- Python 3.10 or higher
- Basic understanding of Python async/await
- Familiarity with HTTP and client-server architecture

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install fastmcp httpx mcp
```

Or use the provided requirements file:
```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python doc_assistant_mcp_server.py
```

You should see output like:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000
```

### 3. Test the Server

In a new terminal:
```bash
python test_client.py
```

## 🏗️ Understanding the Architecture

### MCP Basics

Model Context Protocol (MCP) allows AI assistants to interact with external systems through:
- **Tools**: Functions the AI can call (like `analyze_python_file`)
- **Resources**: Data the AI can read (like documentation templates)
- **Prompts**: Pre-configured conversation starters

### Transport Mechanism

We use HTTP with Server-Sent Events (SSE) for:
- **Stateless operation**: Each request is independent
- **Easy deployment**: Works with standard web infrastructure
- **Real-time updates**: SSE enables streaming responses

## 📝 Step-by-Step Tutorial

### Step 1: Setting Up the MCP Server

Create `doc_assistant_mcp_server.py`:

```python
from fastmcp import FastMCP

# Initialize with HTTP/SSE support
mcp = FastMCP("Code Documentation Assistant", stateless_http=True)
```

The `stateless_http=True` flag enables HTTP transport mode.

### Step 2: Creating Tools

Tools are functions that AI assistants can call. Here's our main tool:

```python
@mcp.tool()
def analyze_python_file(file_path: str) -> Dict[str, any]:
    """
    Analyze a Python file and extract its structure.
    """
    # Parse Python AST
    with open(file_path, 'r') as f:
        content = f.read()
    
    tree = ast.parse(content)
    # Extract classes, functions, etc.
    return analysis_results
```

Key points:
- Use the `@mcp.tool()` decorator
- Include clear docstrings (shown to the AI)
- Return JSON-serializable data

### Step 3: Adding Resources

Resources provide static or dynamic content:

```python
@mcp.resource("documentation://templates/function")
def get_function_template() -> str:
    """Provides a template for function documentation."""
    return "# Function Documentation Template..."
```

Resources use URI-style paths for organization.

### Step 4: Creating Prompts

Prompts help guide AI interactions:

```python
@mcp.prompt()
def document_codebase() -> List[Dict[str, str]]:
    """Prompt to help document an entire codebase."""
    return [
        {"role": "system", "content": "You are a documentation expert..."},
        {"role": "user", "content": "Help me document my codebase..."}
    ]
```

### Step 5: Running the Server

```python
if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)
```

## 🧪 Testing Your Server

The test client demonstrates all features:

```python
# Connect to the server
async with sse_client("http://localhost:8000/sse") as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        
        # List available tools
        tools = await session.list_tools()
        
        # Call a tool
        result = await session.call_tool(
            "analyze_python_file",
            arguments={"file_path": "./example.py"}
        )
```

## 🎥 Video Tutorial Script

### Introduction (0:00-0:30)
"Today we'll build a Code Documentation Assistant using MCP - a practical tool that analyzes your code and generates documentation automatically."

### Overview (0:30-1:30)
1. Show the problem: Undocumented code
2. Demo the solution: Running documentation generation
3. Explain MCP's role

### Building the Server (1:30-5:00)
1. Set up the FastMCP server
2. Implement the `analyze_python_file` tool
3. Add documentation generation tools
4. Create resource templates

### Testing (5:00-6:30)
1. Start the server
2. Run the test client
3. Show generated documentation

### Real-World Usage (6:30-7:30)
1. Analyze a real project
2. Generate README
3. Extract TODOs

### Next Steps (7:30-8:00)
- Adding more languages
- Integrating with IDEs
- Deploying to production

## 🔧 Extending the Server

Ideas for enhancement:
1. **Multi-language support**: Add JavaScript, TypeScript analysis
2. **Git integration**: Document changes between commits
3. **API documentation**: Generate OpenAPI specs
4. **Complexity analysis**: Add code metrics
5. **Diagram generation**: Create UML from code

## 🚢 Deployment Options

### Local Development
```bash
python doc_assistant_mcp_server.py
```

### Production with Gunicorn
```bash
gunicorn doc_assistant_mcp_server:mcp --worker-class uvicorn.workers.UvicornWorker
```

### Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY doc_assistant_mcp_server.py .
CMD ["python", "doc_assistant_mcp_server.py"]
```

## 🔍 Troubleshooting

### Server won't start
- Check port 8000 is available
- Ensure all dependencies are installed
- Verify Python version >= 3.10

### Client connection fails
- Confirm server is running
- Check firewall settings
- Verify correct URL in client

### Tool execution errors
- Add error handling in tools
- Validate input parameters
- Check file permissions

## 📚 Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [FastMCP GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [SSE Specification](https://html.spec.whatwg.org/multipage/server-sent-events.html)

## 🎯 Summary

You've built a practical MCP server that:
- ✅ Uses HTTP/SSE transport for easy deployment
- ✅ Exposes useful tools for code documentation
- ✅ Provides resources and prompts for better AI interaction
- ✅ Demonstrates real-world developer productivity use case

This foundation can be extended to create more sophisticated development tools that integrate seamlessly with AI assistants.