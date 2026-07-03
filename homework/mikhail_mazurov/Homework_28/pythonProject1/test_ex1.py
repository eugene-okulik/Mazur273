from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_field = page.get_by_role('link', name='Form Authentication')
    search_field.click()
    username_field = page.get_by_role('textbox', name='username')
    username_field.press_sequentially('wrong_username', delay=50)
    password_field = page.get_by_role('textbox', name='password')
    password_field.fill('wrong_password')
    page.get_by_role('button', name='Login').click()
    expect(page.get_by_role('heading', name='Your username is invalid!'))
