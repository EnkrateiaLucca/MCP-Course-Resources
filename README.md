# Getting Started with MCP (Model Context Protocol)

A comprehensive course on building AI agent applications using the Model Context Protocol (MCP) - the new open standard for connecting AI assistants to external tools and data sources.

## 🎯 Course Overview

This course teaches you how to build production-ready AI applications using MCP, covering everything from basic concepts to advanced integrations with Claude Code and Cursor. You'll learn to create servers that expose tools, resources, and prompts that AI assistants can use to perform real-world tasks.

## 📚 What You'll Learn

- **MCP Fundamentals**: Understand the architecture, components, and communication flow
- **Building MCP Servers**: Create servers that expose tools, resources, and prompts
- **Client Implementation**: Build clients that connect to MCP servers
- **Transport Protocols**: Master both stdio and HTTP transport mechanisms
- **Real-world Integration**: Deploy MCP servers with Claude Code and Cursor
- **Best Practices**: Security, error handling, and production deployment

## 🚀 Prerequisites

- Python 3.8 or higher
- Basic understanding of Python programming
- Familiarity with async/await concepts (helpful but not required)
- Command line/terminal experience

## 📁 Repository Structure

```
getting-started-with-mcp-repo/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── LICENSE                  # License information
├── lessons/                 # Course lessons (1-8)
│   ├── lesson-1/           # Introduction to MCP
│   ├── lesson-2/           # MCP Components
│   ├── lesson-3/           # Communication Flow
│   ├── lesson-4/           # First MCP Server
│   ├── lesson-5/           # JSON-RPC Protocol
│   ├── lesson-6/           # Building with MCP
│   ├── lesson-7/           # Claude Code Integration
│   └── lesson-8/           # Cursor Integration
├── code-examples/          # Practical implementations
│   ├── 01-basic-server/    # Simple MCP server
│   ├── 02-file-manager/    # File management server
│   ├── 03-http-client/     # HTTP client example
│   └── 04-claude-integration/ # Claude Desktop setup
├── assets/                 # Images and diagrams
├── transcripts/           # Lesson transcripts
├── quizzes/              # Interactive quizzes
└── resources/            # Additional materials
```

## 🛠️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/EnkrateiaLucca/MCP-Course-Resources
cd getting-started-with-mcp-repo
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Your First MCP Server

```bash
cd code-examples/01-basic-server
python mcp_server.py
```

## 📖 Course Curriculum

### Lesson 1: Introduction to MCP
- What is MCP and why it matters
- The AI agent ecosystem
- MCP vs traditional APIs
- Real-world use cases

### Lesson 2: MCP Components & Capabilities
- Understanding Hosts, Clients, and Servers
- Core capabilities: Tools, Resources, Prompts, Sampling
- Component interaction patterns

### Lesson 3: Communication Flow Fundamentals
- Request-response architecture
- Transport layer options
- Message routing and handling

### Lesson 4: Building Your First MCP Server
- Setting up FastMCP
- Creating a simple tool
- Testing with a client
- Hands-on: File creation tool

### Lesson 5: JSON-RPC Message Protocol
- Understanding JSON-RPC 2.0
- Message structure and types
- Error handling patterns
- Protocol extensions

### Lesson 6: Advanced Server Development
- Multi-tool servers
- HTTP transport implementation
- Client-server communication
- Building a file management system

### Lesson 7: Claude Code Integration
- Configuring MCP servers in Claude Code
- Development workflow
- Debugging and testing
- Best practices

### Lesson 8: Cursor Integration
- Setting up MCP with Cursor
- Advanced configurations
- Productivity tips
- Real-world examples

## 💻 Code Examples

### Basic Server (Lesson 4)
```python
from mcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def create_file(path: str, content: str) -> dict:
    """Create a file with specified content"""
    with open(path, 'w') as f:
        f.write(content)
    return {"created": path, "size": len(content)}
```

### File Manager Server (Lesson 6)
- Complete CRUD operations for files
- HTTP transport support
- Error handling and validation
- See `code-examples/02-file-manager/`

### HTTP Client (Lesson 6)
- Connects to MCP servers via HTTP
- Integrates with Claude API
- Interactive chat interface
- See `code-examples/03-http-client/`

## 🔧 Environment Setup

### Required Environment Variables

```bash
# For Claude API integration
export ANTHROPIC_API_KEY="your-api-key"

# For HTTP transport (optional)
export MCP_SERVER_PORT=8000
```

### Installing MCP

```bash
# Basic installation
pip install mcp

# With CLI support
pip install mcp[cli]

# For development
pip install mcp[dev]
```

## 📝 Additional Resources

- [Official MCP Documentation](https://github.com/modelcontextprotocol/protocol)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Code Documentation](https://claude.ai/code)
- [Community Examples](https://github.com/modelcontextprotocol/examples)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Anthropic team for creating MCP
- Course participants for valuable feedback
- Open source community for tooling and libraries

---

**Happy Learning!** 🎉

If you have questions or need help, please open an issue in this repository.
