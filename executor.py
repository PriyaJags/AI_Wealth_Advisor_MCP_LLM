from mcp_client import MCPClient


class Executor:

    def __init__(self):
        self.client = MCPClient()

    def run_tool(self, tool_name, client_name):

        if not tool_name:
            return {"error": "No tool selected"}

        tool_name = tool_name.strip().lower()

        valid_tools = {
            "client_profile",
            "portfolio",
            "risk_assessment"
        }

        if tool_name not in valid_tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        result = self.client.execute(
            tool_name,
            {"client_name": client_name}
        )

        # MCP unwrap
        try:
            if hasattr(result, "content") and result.content:
                return result.content[0].text
            return result
        except:
            return {"error": "MCP failure"}