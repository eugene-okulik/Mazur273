from playwright.sync_api import expect

from pages.base_page2 import BasePage


class ShopPage(BasePage):
    CATEGORY_URL = 'http://testshop.qa-practice.com/shop/category/desks-1'

    def open_category(self):
        self.page.goto(self.CATEGORY_URL)

    def category_is_open(self):
        expect(
            self.page
        ).to_have_url(self.CATEGORY_URL)

    def change_currency_to_eur(self):
        self.page.get_by_role(
            'button',
            name='Benelux'
        ).click()

        eur = self.page.locator(
            '#products_grid a[href*="change_pricelist/3"]'
        ).first

        expect(eur).to_be_visible()

        eur.click()

    def currency_is_eur(self):
        expect(
            self.page.locator('#products_grid')
        ).to_contain_text('€')

    def open_sort_dropdown(self):
        self.page.get_by_role(
            'button',
            name='Featured'
        ).click()

    def sort_products(self, sort_name):
        self.open_sort_dropdown()

        option = self.page.locator(
            '#products_grid a'
        ).filter(
            has_text=sort_name
        ).first

        expect(option).to_be_visible()

        option.click()

    def get_sorted_titles(self):
        titles = self.page.locator(
            '.o_wsale_products_item_title'
        ).all_inner_texts()

        return [
            title.strip().lower()
            for title in titles
            if title.strip()
        ]