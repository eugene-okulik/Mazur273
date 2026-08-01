import json
from playwright.sync_api import Page, expect, Route


def test_yabloko(page: Page):

    def change_req(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = 'яблокофон 17 про'
        route.fulfill(status=response.status, body=json.dumps(body))

    page.route('**/step0_iphone/**', change_req)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.wait_for_load_state('networkidle')

    page.get_by_role("button", name="Take a closer look - iPhone 17 Pro & iPhone 17 Pro Max").click()

    pro_title = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(pro_title).to_have_text('яблокофон 17 про')
