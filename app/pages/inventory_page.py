from app.state import state

class InventoryPage:

    async def open(self):
        if not state.page:
            raise RuntimeError("No active page")
        await state.page.goto("https://www.saucedemo.com/inventory.html")

    async def get_products(self) -> list[tuple[str, str]]:
        if not state.page:
            raise RuntimeError("No active page")

        names = await state.page.locator(".inventory_item_name").all_text_contents()
        prices = await state.page.locator(".inventory_item_price").all_text_contents()

        return list(zip(names, prices))

    async def add_item_to_cart(self, item_name: str):
        if not state.page:
            raise RuntimeError("No active page")

        items = state.page.locator(".inventory_item")
        count = await items.count()

        for i in range(count):
            name = await items.nth(i).locator(".inventory_item_name").text_content()
            if name.strip() == item_name:
                await items.nth(i).locator(".btn_inventory").click()
                return

        raise ValueError(f"Item not found: {item_name}")
