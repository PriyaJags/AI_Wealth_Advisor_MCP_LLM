import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:

    async def call_tool(self, tool_name, arguments):

        server_path = os.path.join(
            os.path.dirname(__file__),
            "mcp_server.py"
        )

        server = StdioServerParameters(
            command="python",
            args=[server_path]
        )

        async with stdio_client(server) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments
                )

                return result

    def execute(self, tool_name, arguments):
        return asyncio.run(
            self.call_tool(tool_name, arguments)
        )