def test_add_complex_product(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    )

    product.add_complex_product_to_cart()

    cart.open()

    assert cart.product_is_visible('Customizable Desk')


def test_change_quantity(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    )

    product.add_complex_product_to_cart()

    cart.wait_counter(1)

    cart.increase_quantity()

    cart.wait_counter(2)

    assert cart.get_product_quantity() == 2


def test_incorrect_discount_code(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    )

    product.add_complex_product_to_cart()

    cart.apply_promo('TEST_PROMO')

    assert cart.get_promo_error() == 'This promo code is not available.'