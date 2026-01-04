# MCP Playwright Automation Framework

This project is a **Model Context Protocol (MCP) server** that exposes a **Playwright-based browser automation framework** as callable tools for Large Language Models (LLMs), such as **Claude Desktop**.

The framework is designed with **clean architecture principles**:
- clear separation of concerns
- Page Object Model
- persistent browser state
- MCP tools as a thin orchestration layer

It enables an LLM to **open a real browser, navigate a web application, perform actions, and verify results**.



## ✨ Key Features

- MCP-compliant server using `FastMCP`
- Playwright (async) browser automation
- Persistent browser session across tool calls
- Page Object Model for maintainability
- Modular tool registration
- Ready for AI-driven testing and automation



## 🔗 Claude Desktop Integration
This MCP server can be connected to Claude Desktop.

- Clone/Download this repository
- Install Claude Desktop
- Create 'claude_desktop_config.json' in the 'AppData\Roaming\Claude' directory
- Add the following content to the 'claude_desktop_config.json' file:

```json
{
  "mcpServers": {
    "playwright-mcp": {
      "command": "F:/mcp_02/.venv/Scripts/python.exe",
      "args": ["main.py"],
      "cwd": "F:/mcp_02"
    }
  }
}
```



## 📁 Project Structure

```text
app/
├── server.py              # MCP server initialization
├── state.py               # Shared application state (browser, page)
│
├── browser/
│   └── browser_manager.py # Browser lifecycle handling
│
├── pages/                 # Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tools/                 # MCP tool definitions
│   ├── browser_tools.py
│   ├── auth_tools.py
│   ├── cart_tools.py
│   └── checkout_tools.py
│
main.py                    # MCP entry point