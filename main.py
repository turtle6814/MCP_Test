import requests
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def download_webpage_as_markdown(url: str) -> str:
    """
    Download the content of any web page in markdown format.
    Uses Jina AI's reader service to convert web pages to markdown.

    Args:
        url: The URL of the web page to download (e.g., 'https://example.com')

    Returns:
        The content of the web page in markdown format
    """
    # Prepend r.jina.ai/ to the URL
    jina_url = f"https://r.jina.ai/{url}"

    try:
        response = requests.get(jina_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error downloading webpage: {str(e)}"


# Register the tool with MCP
mcp.tool(download_webpage_as_markdown)

if __name__ == "__main__":
    mcp.run()
