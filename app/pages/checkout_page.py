from app.state import state

class CheckoutPage:

    async def fill_information(self, first_name: str, last_name: str, postal_code: str):
        if not state.page:
            raise RuntimeError("No active page")

        await state.page.fill("#first-name", first_name)
        await state.page.fill("#last-name", last_name)
        await state.page.fill("#postal-code", postal_code)
        await state.page.click("#continue")

    async def verify_overview(
        self,
        expected_product: str,
        expected_item_total: float,
        expected_tax: float,
        expected_total: float
    ) -> str:

        if not state.page:
            return "FAIL: No active page"

        product = await state.page.text_content(".inventory_item_name")
        if product.strip() != expected_product:
            return f"FAIL: Product mismatch ({product})"

        item_total = float(
            (await state.page.text_content(".summary_subtotal_label"))
            .replace("Item total: $", "")
        )

        tax = float(
            (await state.page.text_content(".summary_tax_label"))
            .replace("Tax: $", "")
        )

        total = float(
            (await state.page.text_content(".summary_total_label"))
            .replace("Total: $", "")
        )

        if item_total != expected_item_total:
            return f"FAIL: Item total mismatch ({item_total})"
        if tax != expected_tax:
            return f"FAIL: Tax mismatch ({tax})"
        if total != expected_total:
            return f"FAIL: Total mismatch ({total})"

        return "PASS: Checkout overview is correct"

    async def finalize(self) -> str:
        if not state.page:
            return "FAIL: No active page"

        await state.page.click("#finish")
        await state.page.wait_for_selector(".complete-header")
        confirmation = await state.page.text_content(".complete-header")
        return f"Order completed: {confirmation.strip()}"
