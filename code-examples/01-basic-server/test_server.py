import asyncio
import sys
from mcp.server.fastmcp import FastMCP

# Import the server
sys.path.append('.')
from mcp_server import mcp

async def test_tool():
    """Test the create_file tool directly"""
    # Get the tool
    tools = mcp._tool_manager._tools
    create_file_tool = tools.get("create_file")
    
    if create_file_tool:
        print("Found create_file tool!")
        print(f"Description: {create_file_tool.description}")
        
        # Test creating a file
        result = create_file_tool.fn(
            file_path="test_output.txt",
            content="Hello from MCP test!"
        )
        print(f"Tool result: {result}")
        
        # Verify file was created
        try:
            with open("test_output.txt", "r") as f:
                content = f.read()
                print(f"File content: {content}")
                print("✅ Test passed! File was created successfully.")
        except FileNotFoundError:
            print("❌ Test failed! File was not created.")
    else:
        print("❌ create_file tool not found!")

if __name__ == "__main__":
    asyncio.run(test_tool())