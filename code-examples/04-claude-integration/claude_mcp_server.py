from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lucas-top3-foods")

@mcp.tool()
def print_lucas_top_3_foods() -> str:
    """
    This tool prints Lucas's top 3 foods.
    """
    return "Pancakes, Pizza, and Ribs"

if __name__ == "__main__":
    mcp.run()