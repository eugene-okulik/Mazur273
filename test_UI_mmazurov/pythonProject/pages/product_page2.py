from playwright.sync_api import expect

from pages.base_page2 import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = '#add_to_cart'
    CART_COUNTER = 'sup.my_cart_quantity'

    TERMS_LINK = 'a[href="/terms"]'
    SIGN_IN_LINK = 'a[href="/web/login"]'

    def add_simple_product_to_cart(self):
        add_to_cart = self.page.locator(self.ADD_TO_CART)

        expect(add_to_cart).to_be_visible()
        expect(add_to_cart).to_be_enabled()

        add_to_cart.click()

        expect(
            self.page.locator(self.CART_COUNTER).first
        ).to_have_text('1')

    def add_complex_product_to_cart(self):
        add_to_cart = self.page.locator(self.ADD_TO_CART)

        expect(add_to_cart).to_be_visible()
        expect(add_to_cart).to_be_enabled()

        add_to_cart.click()

        proceed_to_checkout = self.page.get_by_role(
            'button',
            name='Proceed to Checkout'
        )

        expect(proceed_to_checkout).to_be_visible()
        expect(proceed_to_checkout).to_be_enabled()

        proceed_to_checkout.click()

        self.page.wait_for_url('**/shop/cart*')

    def click_terms_link(self):
        terms = self.page.locator(
            self.TERMS_LINK
        ).filter(
            has_text='Terms'
        ).first

        expect(terms).to_be_visible()

        terms.click()

        self.page.wait_for_url('**/terms')

    def click_sign_in_link(self):
        sign_in = self.page.locator(
            self.SIGN_IN_LINK
        ).filter(
            has_text='Sign in'
        ).first

        expect(sign_in).to_be_visible()

        sign_in.click()

        self.page.wait_for_url('**/web/login')

    def get_current_url(self):
        return self.page.url