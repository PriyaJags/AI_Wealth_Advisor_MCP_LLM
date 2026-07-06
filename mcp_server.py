from mcp.server.fastmcp import FastMCP

from tools import (
    get_client_profile,
    get_portfolio,
    get_risk_assessment,
)

mcp = FastMCP("wealth-advisor")


@mcp.tool()
def client_profile(client_name: str):
    """Get complete client profile."""
    return get_client_profile(client_name)


@mcp.tool()
def portfolio(client_name: str):
    """Get client portfolio."""
    return get_portfolio(client_name)


@mcp.tool()
def risk_assessment(client_name: str):
    """Get client's risk assessment."""
    return get_risk_assessment(client_name)


if __name__ == "__main__":
    mcp.run()