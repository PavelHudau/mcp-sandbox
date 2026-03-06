from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Polite Greeting MCP")

@mcp.tool()
def greet_me(name: str) -> str:
    """
    Greet a user by name.
    
    Args:
        name (str): The name of the user to greet.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
