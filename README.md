# MCP Test Project

A Model Context Protocol (MCP) server with web content downloading and document search capabilities.

## Features

### 1. MCP Server with Custom Tools

The project includes a FastMCP server ([`main.py`](main.py )) with the following tools:

- **`add(a, b)`** - Simple addition of two numbers
- **`download_webpage_as_markdown(url)`** - Downloads any webpage content in markdown format using Jina AI's reader service

#### How it works

The `download_webpage_as_markdown` tool prepends `r.jina.ai/` to any URL, which converts the webpage to clean markdown format.


### 2. Document Indexing and Search

The project includes functionality to index and search markdown documentation ([`index_docs.py`](index_docs.py )):

- Downloads the FastMCP repository documentation
- Extracts `.md` and `.mdx` files from the zip archive
- Removes path prefixes for clean filenames
- Indexes content using [minsearch](https://github.com/alexeygrigorev/minsearch)
- Provides semantic search across documentation

#### Features:
- **Smart downloading**: Only downloads the zip file if it doesn't exist
- **Markdown extraction**: Processes all `.md` and `.mdx` files
- **Path normalization**: Converts `fastmcp-main/docs/file.md` to `docs/file.md`
- **Full-text search**: Search across both content and filenames

## Installation

1. Install dependencies:
```bash
uv sync
```

This will install:
- `fastmcp` - MCP server framework
- `requests` - HTTP library
- `minsearch` - Lightweight search engine

## Usage

### Running the MCP Server

```bash
uv run main.py
```

### Testing Web Content Download

Run the test to download a GitHub repository page:

```bash
python test.py
```

This downloads `https://github.com/alexeygrigorev/minsearch` and saves the markdown content to `downloaded_content.md`.


## Project Structure

```
MCP_Test/
├── main.py              # MCP server with tools
├── index_docs.py        # Document indexing and search functions
├── search.py            # Search test implementation
├── test.py              # Web download test
├── count_data.py        # Word counting example
├── pyproject.toml       # Project dependencies
└── README.md            # README file
```

## How to Use with GitHub Copilot

To integrate this MCP server with GitHub Copilot in VS Code:

1. Install the "Prompt CDS MCP Client" extension
2. Open GitHub Copilot Chat settings
3. Add the MCP server configuration:

```json
{
  "mcpServers": {
    "demo": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/homework",
        "run",
        "main.py"
      ]
    }
  }
}
```

4. Restart VS Code

Once configured, GitHub Copilot can use your custom tools directly in conversation.

## API Reference

### `download_webpage_as_markdown(url: str) -> str`

Downloads and converts a webpage to markdown format.

**Parameters:**
- `url` (str): The URL of the webpage to download

**Returns:**
- str: The webpage content in markdown format, or an error message

**Example:**
```python
content = download_webpage_as_markdown('https://example.com')
```

### `search(index, query: str, num_results: int = 5) -> list`

Searches the document index for relevant results.

**Parameters:**
- `index`: The minsearch Index object
- `query` (str): The search query
- `num_results` (int): Number of results to return (default: 5)

**Returns:**
- list: List of document dictionaries with 'filename' and 'content' fields


## Dependencies

- **Python**: >=3.10
- **fastmcp**: >=2.14.1 - MCP server framework
- **requests**: >=2.31.0 - HTTP requests
- **minsearch**: >=0.0.3 - Search engine

## License

This is a demo project for learning MCP (Model Context Protocol).
