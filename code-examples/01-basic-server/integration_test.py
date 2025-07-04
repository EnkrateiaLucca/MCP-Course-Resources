#!/usr/bin/env python3
import asyncio
import subprocess
import sys
import time
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_integration():
    """Test the MCP server integration"""
    # Start the server as a subprocess
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            # List available tools
            tools_response = await session.list_tools()
            tools = tools_response.tools
            print(f"Available tools: {[tool.name for tool in tools]}")
            
            # Test the create_file tool
            if tools:
                tool_name = tools[0].name
                print(f"\nTesting tool: {tool_name}")
                
                # Call the tool
                result = await session.call_tool(
                    tool_name, 
                    {"file_path": "integration_test_output.txt", "content": "Integration test successful!"}
                )
                
                print(f"Tool result: {result}")
                
                # Verify the file was created
                try:
                    with open("integration_test_output.txt", "r") as f:
                        content = f.read()
                        print(f"\nFile content: {content}")
                        print("✅ Integration test PASSED!")
                        return True
                except FileNotFoundError:
                    print("❌ Integration test FAILED - file not created")
                    return False
            else:
                print("❌ No tools found!")
                return False

if __name__ == "__main__":
    success = asyncio.run(test_integration())
    sys.exit(0 if success else 1)