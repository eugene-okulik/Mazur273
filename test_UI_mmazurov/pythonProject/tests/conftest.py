import pytest
from playwright.sync_api import sync_playwright

from pages.cart_page2 import CartPage
from pages.product_page2 import ProductPage
from pages.shop_page2 import ShopPage


@pytest.fixture()
def page():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    yield page

    browser.close()
    playwright.stop()


@pytest.fixture()
def cart(page):
    return CartPage(page)


@pytest.fixture()
def shop(page):
    return ShopPage(page)


@pytest.fixture()
def product(page):
    return ProductPage(page)