from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    # options = Options()
    # options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_form_fill(driver):
    input_data = ['Mik', 'Maz', 'example@mail.ge', '9951234567', 'Arts',
                  'Pushkina st., Kalatushlina house', '01 May 1953']
    driver.get('https://demoqa.com/automation-practice-form')

    search_name_input = driver.find_element(By.ID, 'firstName')
    search_name_input.send_keys(input_data[0])

    search_lastname_input = driver.find_element(By.ID, 'lastName')
    search_lastname_input.send_keys(input_data[1])

    search_email_input = driver.find_element(By.ID, 'userEmail')
    search_email_input.send_keys(input_data[2])

    search_number_input = driver.find_element(By.ID, 'userNumber')
    search_number_input.send_keys(input_data[3])

    search_gender_input = driver.find_element(By.CSS_SELECTOR, '#gender-radio-3')
    search_gender_input.click()

    search_subj_input = driver.find_element(By.ID, 'subjectsInput')
    search_subj_input.click()

    search_subj_input.send_keys(input_data[4])
    search_subj_input.send_keys(Keys.ENTER)

    search_address_input = driver.find_element(By.ID, 'currentAddress')
    search_address_input.send_keys(input_data[5])

    search_address_input = driver.find_element(By.ID, 'dateOfBirthInput')
    search_address_input.click()
    driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('January')
    driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('2001')
    driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--001').click()

    search_hobbie1_input = driver.find_element(By.ID, 'hobbies-checkbox-1')
    search_hobbie1_input.click()

    search_hobbie3_input = driver.find_element(By.ID, 'hobbies-checkbox-3')
    search_hobbie3_input.click()

    search_dropdown1 = driver.find_element(By.ID, 'react-select-3-input')
    search_dropdown1.send_keys('NC')
    search_dropdown1.send_keys(Keys.ENTER)

    search_dropdown1 = driver.find_element(By.ID, 'react-select-4-input')
    search_dropdown1.send_keys('No')
    search_dropdown1.send_keys(Keys.ENTER)

    submit = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].click();", submit)

    # modal_window = driver.find_element(By.ID, 'example-modal-sizes-title-lg')
    # assert modal_window.text == 'Thanks for submitting the form'

    data = driver.find_element(By.CLASS_NAME, 'table-responsive')
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
    print(data.text)
