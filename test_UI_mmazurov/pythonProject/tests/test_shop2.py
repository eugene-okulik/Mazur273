def test_open_category(shop):
    shop.open_category()

    shop.category_is_open()


def test_change_currency(shop):
    shop.open_category()

    shop.change_currency_to_eur()

    shop.currency_is_eur()


def test_sort_by_name(shop):
    shop.open_category()

    shop.sort_products('Name (A-Z)')

    shop.check_products_sorted_by_name()
