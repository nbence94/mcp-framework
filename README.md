# MCP Playwright Test Server

This project is a **FastMCP-based automation server** that combines **Playwright browser automation** and **web content extraction**.  
It exposes reusable tools that allow an AI client to control a real browser, interact with a demo webshop (Sauce Demo), and validate checkout flows end-to-end.

The server keeps the browser **stateful and persistent**, enabling multi-step workflows (open → login → add to cart → checkout → verify → finish).

---

## Features

- Headed Chromium browser automation via Playwright
- Stateful browser session management
- Web page text extraction via HTTP + BeautifulSoup
- Full Sauce Demo shopping and checkout flow automation
- Designed for MCP-compatible AI clients

---

## Available Tools

### `ExtractWebContent`
Extracts and cleans all visible text from a given URL using HTTP requests and BeautifulSoup.

### `OpenBrowser`
Launches a Chromium browser (non-headless) and navigates to a URL.  
Keeps the browser open for subsequent steps.

### `CloseBrowser`
Closes the currently running browser and cleans up resources.

### `LoginToSauceDemo`
Logs into https://www.saucedemo.com using the default demo credentials.

### `GetProducts`
Retrieves all available products from the inventory page with their prices.

### `AddItemToCart`
Adds a specific product to the cart by exact product name.

### `CheckItemInCart`
Verifies whether a given product is present in the shopping cart.

### `ClickCheckout`
Navigates to the cart and starts the checkout process.

### `FillCheckoutInfo`
Fills out the checkout form (first name, last name, postal code).

### `ClickContinue`
Continues from the checkout information page to the overview page.

### `VerifyCheckoutOverview`
Validates:
- Product name  
- Item total  
- Tax  
- Final total  

Returns a PASS / FAIL result with details.

### `FinalizeOrder`
Finishes the purchase and confirms successful order completion.

---

## Running the Server

```bash
python server.py
