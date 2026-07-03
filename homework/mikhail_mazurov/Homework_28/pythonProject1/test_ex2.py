from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    name_field = page.get_by_placeholder('First Name')
    name_field.press_sequentially('Mikhail')
    name_field = page.get_by_placeholder('Last Name')
    name_field.press_sequentially('Mzrv')

    gender_checkbox = page.locator('//*[@id="gender-radio-1"]')
    gender_checkbox.click()

    page.get_by_placeholder('name@example.com').fill('usermailw@mail.ru')
    page.get_by_placeholder('Mobile Number').fill('0123456789')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.press('Control+a')
    date_of_birth.fill('12 Dec 1992')

    subjects = page.locator('.subjects-auto-complete__input-container')
    subjects.click()
    subjects.press_sequentially('Ar')
    subjects.press('Enter')

    page.locator('#hobbies-checkbox-2').check()

    page.get_by_placeholder('Current Address').fill('ul.Pushkina, dom Kalatushkina')

    page.locator("#state").click()
    page.get_by_role("option", name="Rajasthan").click()

    page.locator("#city").click()
    page.get_by_role("option", name="Jaiselmer").click()

    submit_btn = page.get_by_role("button", name="Submit")
    submit_btn.click()

    expect(page.locator('#example-modal-sizes-title-lg'))
