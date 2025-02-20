# OpenAI MCP Server

Query OpenAI models directly from Claude using MCP protocol. This fork adds support for o3-mini and gpt-4o-mini models with improved message handling.

## Features

- Direct integration with OpenAI's API
- Support for multiple models:
  - o3-mini (default): Optimized for concise responses
  - gpt-4o-mini: Enhanced model for more detailed responses
- Configurable message formatting
- Error handling and logging
- Simple interface through MCP protocol

## Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/thadius83/mcp-server-openai.git
cd mcp-server-openai

# Install dependencies
pip install -e .
```

2. **Configure Claude Desktop**:
   
Add this server to your existing MCP settings configuration. Note: Keep any existing MCP servers in the configuration - just add this one alongside them.

Location:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`
- Linux: Check your home directory (`~/`) for the default MCP settings location

```json
{
  "mcpServers": {
    // ... keep your existing MCP servers here ...
    
    "github.com/thadius83/mcp-server-openai": {
      "command": "python",
      "args": ["-m", "src.mcp_server_openai.server", "--openai-api-key", "your-key-here"],
      "env": {
        "PYTHONPATH": "/path/to/your/mcp-server-openai"
      }
    }
  }
}
```

3. **Get an OpenAI API Key**:
   - Visit [OpenAI's website](https://openai.com)
   - Create an account or log in
   - Navigate to API settings
   - Generate a new API key
   - Add the key to your configuration file as shown above

4. **Restart Claude**:
   - After updating the configuration, restart Claude for the changes to take effect

## Usage

The server provides a single tool `ask-openai` that can be used to query OpenAI models. You can use it directly in Claude with the use_mcp_tool command:

```xml
<use_mcp_tool>
<server_name>github.com/thadius83/mcp-server-openai</server_name>
<tool_name>ask-openai</tool_name>
<arguments>
{
  "query": "What are the key features of Python's asyncio library?",
  "model": "o3-mini"  // Optional, defaults to o3-mini
}
</arguments>
</use_mcp_tool>
```

### Model Comparison

1. o3-mini (default)
   - Best for: Quick, concise answers
   - Style: Direct and efficient
   - Example response:
     ```
     Python's asyncio provides non-blocking, collaborative multitasking. Key features:
     1. Event Loop – Schedules and runs asynchronous tasks
     2. Coroutines – Functions you can pause and resume
     3. Tasks – Run coroutines concurrently
     4. Futures – Represent future results
     5. Non-blocking I/O – Efficient handling of I/O operations
     ```

2. gpt-4o-mini
   - Best for: More comprehensive explanations
   - Style: Detailed and thorough
   - Example response:
     ```
     Python's asyncio library provides a comprehensive framework for asynchronous programming.
     It includes an event loop for managing tasks, coroutines for writing non-blocking code,
     tasks for concurrent execution, futures for handling future results, and efficient I/O
     operations. The library also provides synchronization primitives and high-level APIs
     for network programming.
     ```

### Response Format

The tool returns responses in a standardized format:
```json
{
  "content": [
    {
      "type": "text",
      "text": "Response from the model..."
    }
  ]
}
```

## Troubleshooting

1. **Server Not Found**:
   - Verify the PYTHONPATH in your configuration points to the correct directory
   - Ensure Python and pip are properly installed
   - Try running `python -m src.mcp_server_openai.server --openai-api-key your-key-here` directly to check for errors

2. **Authentication Errors**:
   - Check that your OpenAI API key is valid
   - Ensure the key is correctly passed in the args array
   - Verify there are no extra spaces or characters in the key

3. **Model Errors**:
   - Confirm you're using supported models (o3-mini or gpt-4o-mini)
   - Check your query isn't empty
   - Ensure you're not exceeding token limits

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest -v test_openai.py -s
```

## Changes from Original

- Added support for o3-mini and gpt-4o-mini models
- Improved message formatting
- Removed temperature parameter for better compatibility
- Updated documentation with detailed usage examples
- Added model comparison and response examples
- Enhanced installation instructions
- Added troubleshooting guide

## License

MIT License
