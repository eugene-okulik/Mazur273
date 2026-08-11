def test_add_complex_product(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    )

    product.add_complex_product_to_cart()

    cart.check_counter(1)
    cart.product_is_visible('Customizable Desk')


def test_change_quantity(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/furn-9999-office-design-software-7?category=9'
    )

    product.add_simple_product_to_cart()

    cart.open()
    cart.change_quantity(2)
    cart.check_counter(2)


def test_incorrect_discount_code(product, cart):
    product.open(
        'http://testshop.qa-practice.com/shop/customizable-desk-9#attr=1,3'
    )

    product.add_complex_product_to_cart()

    cart.apply_promo('TEST_PROMO')

    cart.check_promo_error(
        'This promo code is not available.'
    )
