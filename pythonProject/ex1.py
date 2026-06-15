from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_new_tab(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)

    link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

    wait.until(lambda d: len(d.window_handles) == 2)
    driver.switch_to.window(driver.window_handles[1])

    result = driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]')
    assert result.text == 'Customizable Desk'

    driver.find_element(By.ID, 'add_to_cart').click()

    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-content .btn-secondary')))
    continue_btn.click()
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.my_cart_quantity'),
            '1'
        )
    )

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    cart = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.fa-shopping-cart'))
    )
    cart.click()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.d-inline'))
    )

    assert 'Customizable Desk' in driver.find_element(
        By.CSS_SELECTOR,
        '.d-inline'
    ).text
