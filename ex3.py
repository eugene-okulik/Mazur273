from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
import pytest

@pytest.fixture()
def driver():
    # options = Options()
    # options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_chose_lang(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    search_dropdown = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(search_dropdown)
    dropdown.select_by_visible_text('Python')
    driver.find_element(By.NAME, 'submit').click()
    result_text = driver.find_element(By.CLASS_NAME, 'result-text')
    print(result_text.text)


def test_hello_world_check(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start = driver.find_element(By.XPATH, '//*[@id="start"]/button')
    start.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'finish'), 'Hello World!'))
    hello_world = driver.find_element(By.ID, 'finish')
    assert hello_world.text == 'Hello World!'
