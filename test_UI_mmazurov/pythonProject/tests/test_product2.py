def test_add_product(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9'
    )

    product.add_simple_product_to_cart()

    cart.open()

    assert cart.product_is_visible(
        'Office Design Software'
    )


def test_terms_link(product):
    product.open(
        'http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9'
    )

    product.click_terms_link()

    assert (
        product.get_current_url()
        == 'http://testshop.qa-practice.com/terms'
    )


def test_sign_in_link(product):
    product.open(
        'http://testshop.qa-practice.com'
    )

    product.click_sign_in_link()

    assert (
        product.get_current_url()
        == 'http://testshop.qa-practice.com/web/login'
    )
