from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-mcp-server")

@mcp.tool()
def create_file(file_path: str, content: str)-> dict[str, str]:
    """
    Create a file with the given path and content.
    """
    with open(file_path, "w") as f:
        f.write(content)
    return {file_path: content}

if __name__ == "__main__":
    mcp.run(transport="stdio")