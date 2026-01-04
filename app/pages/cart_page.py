from app.state import state

class CartPage:

    async def open(self):
        if not state.page:
            raise RuntimeError("No active page")
        await state.page.click(".shopping_cart_link")

    async def is_item_in_cart(self, item_name: str) -> bool:
        if not state.page:
            raise RuntimeError("No active page")

        items = state.page.locator(".cart_item")
        count = await items.count()

        for i in range(count):
            text = await items.nth(i).text_content()
            if item_name in text:
                return True

        return False

    async def click_checkout(self):
        if not state.page:
            raise RuntimeError("No active page")

        await state.page.click("#checkout")
