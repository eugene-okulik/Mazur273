import pytest


@pytest.fixture
def product(page):
    from pages.product_page2 import ProductPage

    return ProductPage(page)


@pytest.fixture
def cart(page):
    from pages.cart_page2 import CartPage

    return CartPage(page)


@pytest.fixture
def shop(page):
    from pages.shop_page2 import ShopPage

    return ShopPage(page)
