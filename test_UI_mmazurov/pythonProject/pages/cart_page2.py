from playwright.sync_api import expect
from pages.base_page2 import BasePage


class CartPage(BasePage):
    COUNTER = 'sup.my_cart_quantity'

    PROMO_INPUT = (
        'input[name="promo"], '
        'input[name="coupon"], '
        'input[placeholder*="Promo"], '
        'input[placeholder*="promo"]'
    )

    APPLY_BTN = 'a:has-text("Apply")'
    ERROR_ALERT = 'div.alert.alert-danger'

    QUANTITY_INPUT = (
        'input.js_quantity, '
        'input[name="quantity"], '
        'input[class*="quantity"]'
    )

    def open(self):
        self.page.goto(
            'http://testshop.qa-practice.com/shop/cart'
        )

        self.page.wait_for_load_state('networkidle')

    def get_counter(self):
        counter = self.page.locator(
            f'{self.COUNTER}:visible'
        ).first

        if not counter.is_visible():
            return 0

        text = counter.inner_text().strip()

        return int(text) if text else 0

    def check_counter(self, expected_value):
        counter = self.page.locator(
            f'{self.COUNTER}:visible'
        ).first

        expect(counter).to_have_text(str(expected_value))

    def wait_counter(self, value):
        counter = self.page.locator(
            f'{self.COUNTER}:visible'
        ).first

        expect(counter).to_have_text(str(value))

    def product_is_visible(self, product_name):
        product = self.page.get_by_text(
            product_name,
            exact=False
        ).first

        expect(product).to_be_visible()

    def change_quantity(self, quantity):
        quantity_input = self.page.locator(
            self.QUANTITY_INPUT
        ).first

        expect(quantity_input).to_be_visible()

        quantity_input.fill(str(quantity))
        quantity_input.press('Enter')

        self.page.wait_for_load_state('networkidle')

    def apply_promo(self, code):
        promo_input = self.page.get_by_role(
            'textbox',
            name='Discount code...'
        )

        expect(promo_input).to_be_visible()

        promo_input.fill(code)

        apply_button = self.page.get_by_role(
            'button',
            name='Apply'
        )

        expect(apply_button).to_be_visible()

        apply_button.click()

    def check_promo_error(self, expected_text):
        error = self.page.locator(
            self.ERROR_ALERT
        ).first

        expect(error).to_be_visible()
        expect(error).to_have_text(expected_text)
