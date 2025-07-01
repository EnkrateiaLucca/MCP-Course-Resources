# Connecting MCP Servers to Cursor Editor

## Learning Objectives

By the end of this lesson, you will be able to:
- Configure MCP servers in Cursor editor
- Understand the connection process between MCP servers and Cursor
- Use MCP tools within Cursor's Agent Chat interface

## Introduction

In the previous lesson, we learned how to set up an MCP server and connect it to Claude Code CLI. In this lesson, we'll accomplish the same goal but with a different editor: **Cursor Editor**.

Cursor is a powerful fork of VS Code specifically designed for writing code with AI assistance. This lesson assumes you have basic familiarity with Cursor. If you're new to Cursor, consider taking a dedicated Cursor course first.

## Setting Up MCP Servers in Cursor

### Step 1: Access Cursor Settings

1. Open the Command Palette (usually `Cmd/Ctrl + Shift + P`)
2. Type "cursor settings" and select it
3. Navigate to **Tools and Integrations**

### Step 2: Add a Custom MCP Tool

If you don't have any MCP tools already configured:
1. Click on "Add Custom MCP Tool"
2. This will open an `mcp.json` file where all your MCP servers will be configured

### Step 3: Configure the MCP Server

The `mcp.json` file contains all MCP servers that will be accessible through Cursor's Agent Chat mode. Here's the structure you need to follow:

```json
{
  "lucas-top-three-foods": {
    "command": "/path/to/python",
    "args": ["/path/to/cloud-mcp-server.py"]
  }
}
```

Let's break down each component:

#### Server Name
- Choose a descriptive name for your server (e.g., "lucas-top-three-foods")
- This name will identify your server within Cursor

#### Command Key
- Specifies the path to the Python executable that runs your MCP server
- To find your Python path, run `which python` in your terminal
- Copy and paste the full path into the command field

#### Arguments (args)
- Contains a list of strings with all arguments needed to run the MCP server
- In most cases, this is simply the path to your MCP server Python file
- Right-click your server file → Copy Path → Paste in the args array

### Step 4: Verify the Connection

After saving the configuration:
1. Return to Cursor Settings
2. Check that your MCP tool appears with the correct name
3. Look for the status indicator:
   - **Green dot**: Connected and ready
   - **Yellow/Red dot**: Connection issue

If you see a yellow or red status indicator, reload Cursor to ensure the MCP server initializes properly.

## Using MCP Tools in Cursor

### Accessing Agent Chat

1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Type "Open New Agent Chat"
3. The Agent Chat interface will open on the right side of your editor

### Running MCP Tools

When you want to use an MCP tool:
1. Type your query in the Agent Chat
2. Explicitly mention the MCP tool (e.g., "What are Lucas's top three foods? Use the MCP tool")
3. Cursor will request permission to run the tool
4. Click "Run" to execute the tool
5. The results will appear in the chat interface

## Important Notes

- **Permission Required**: Cursor always asks for permission before running MCP tools for security
- **Explicit Tool Mention**: For best results, explicitly mention that you want to use the MCP tool in your query
- **Environment Matters**: Ensure your Python environment has all necessary dependencies installed

## Troubleshooting

If your MCP server isn't working:
1. Check the status indicator in Cursor Settings
2. Verify your Python path is correct
3. Ensure the MCP server file path is accurate
4. Reload Cursor if necessary
5. Check that your MCP server runs correctly outside of Cursor first

## Summary

Setting up MCP servers in Cursor involves:
1. Creating an `mcp.json` configuration file
2. Specifying the server name, Python command, and server file path
3. Verifying the connection in Cursor Settings
4. Using the Agent Chat interface to interact with your MCP tools

This integration allows you to leverage custom MCP servers directly within your coding environment, enhancing your AI-assisted development workflow.

## Next Steps

- Try creating your own custom MCP servers
- Explore more complex MCP server configurations
- Integrate multiple MCP servers for different purposes
- Learn about advanced Cursor features to maximize your productivity