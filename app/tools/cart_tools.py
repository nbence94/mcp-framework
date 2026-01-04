from mcp.server.fastmcp import FastMCP
from app.pages.inventory_page import InventoryPage
from app.pages.cart_page import CartPage

def register_cart_tools(mcp: FastMCP):

    @mcp.tool(
        name="AddItemToCart",
        description="Add an item to the cart by name"
    )
    async def add_item(item_name: str) -> str:
        inventory = InventoryPage()
        await inventory.add_item_to_cart(item_name)
        return f"Added item to cart: {item_name}"

    @mcp.tool(
        name="CheckItemInCart",
        description="Check if an item is present in the cart"
    )
    async def check_item(item_name: str) -> str:
        cart = CartPage()
        await cart.open()
        exists = await cart.is_item_in_cart(item_name)
        return f"Item '{item_name}' is {'in' if exists else 'not in'} the cart"

    @mcp.tool(
        name="ClickCheckout",
        description="Start checkout from the cart"
    )
    async def click_checkout() -> str:
        cart = CartPage()
        await cart.open()
        await cart.click_checkout()
        return "Checkout started"
