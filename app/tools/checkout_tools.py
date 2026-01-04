from mcp.server.fastmcp import FastMCP
from app.pages.checkout_page import CheckoutPage

def register_checkout_tools(mcp: FastMCP):

    @mcp.tool(
        name="FillCheckoutInfo",
        description="Fill checkout form with user data"
    )
    async def fill_info(first_name: str, last_name: str, postal_code: str) -> str:
        checkout = CheckoutPage()
        await checkout.fill_information(first_name, last_name, postal_code)
        return "Checkout information filled"

    @mcp.tool(
        name="VerifyCheckoutOverview",
        description="Verify checkout overview values"
    )
    async def verify(
        expected_product_name: str,
        expected_item_total: float,
        expected_tax: float,
        expected_total: float
    ) -> str:
        checkout = CheckoutPage()
        return await checkout.verify_overview(
            expected_product_name,
            expected_item_total,
            expected_tax,
            expected_total
        )

    @mcp.tool(
        name="FinalizeOrder",
        description="Finish the checkout process"
    )
    async def finalize() -> str:
        checkout = CheckoutPage()
        return await checkout.finalize()
