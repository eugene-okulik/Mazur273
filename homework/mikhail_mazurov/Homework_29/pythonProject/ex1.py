from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep


def test_arert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    click_btn = page.locator('#content > a.a-button')
    click_btn.click()

    def accept(alert: Dialog):
        alert.accept()

    result_text = page.locator('#result-text')
    expect(result_text).to_contain_text('Ok')
# Тест должен падать, так как Ok и Cancel перепутаны и выполняя alert.accept выбирается Cancel


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    page_2 = new_page_event.value
    result = page_2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_btn = page.locator('#colorChange')
    expect(color_btn).to_contain_class('text-danger', timeout=6000)
    color_btn.click()
