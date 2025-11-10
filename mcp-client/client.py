from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

serve_params = StdioServerParameters(
    command="Uv",
    args=["run", "../mcp-server/weather.py"],
)

async def run():
    try:
        async with stdio_client(serve_params) as (reader, writer):
            print("Client connected to server.")
            async with ClientSession(reader, writer) as session:
                print("Initializing session...")
                await session.initialize()

                print("Listing available tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)


                location = "New York"
                result = await session.call_tool("get_weather", arguments={"location": location})
                print(f"Weather in {location}: {result}")
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()  


if __name__ == "__main__":
    asyncio.run(run())
