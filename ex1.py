from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_find_by_name(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_data = 'cat'
    search_input = driver.find_element(By.CSS_SELECTOR, '[placeholder = "Submit me"]')
    search_input.send_keys(input_data)
    search_input.submit()
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    # assert result_text.text == input_data
    # print(result_text.get_attribute('innerText'))
    print(result_text.text)
