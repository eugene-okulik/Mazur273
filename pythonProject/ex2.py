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


def test_in_shop2(driver):
    driver.get('http://testshop.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    cart_button = driver.find_element(By.CSS_SELECTOR, '[title="Shopping cart"]')

    actions = ActionChains(driver)
    actions.move_to_element(link)
    actions.move_to_element(cart_button)
    actions.click()
    actions.perform()

    driver.implicitly_wait(3)
    assert 'Customizable Desk' in driver.find_element(
        By.CLASS_NAME, 'product_display_name'
    ).text
