from playwright.sync_api import expect

from pages.base_page2 import BasePage


class CartPage(BasePage):
    CART_URL = 'http://testshop.qa-practice.com/shop/cart'

    COUNTER = 'sup.my_cart_quantity'
    PROMO_ERROR = 'div.alert.alert-danger'

    def open(self):
        self.page.goto(self.CART_URL)

    def get_counter(self):
        counter = self.page.locator(
            self.COUNTER
        ).first

        if not counter.is_visible():
            return 0

        text = counter.inner_text().strip()

        return int(text) if text else 0

    def wait_counter(self, value):
        expect(
            self.page.locator(
                self.COUNTER
            ).first
        ).to_have_text(str(value))

    def product_is_visible(self, product_name):
        product = self.page.get_by_role(
            'link',
            name=product_name,
            exact=False
        ).first

        expect(product).to_be_visible()

        return True

    def increase_quantity(self):
        add_one = self.page.get_by_role(
            'link',
            name='Add one'
        )

        expect(add_one).to_be_visible()

        add_one.click()

    def get_product_quantity(self):
        quantity = self.page.get_by_role(
            'textbox'
        ).last

        return int(quantity.input_value())

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

    def get_promo_error(self):
        error = self.page.locator(
            self.PROMO_ERROR
        )

        expect(error).to_be_visible()

        return error.inner_text().strip()