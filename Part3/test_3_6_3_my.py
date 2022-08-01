import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

#pytest.mark.xfail(reason = 'test')
@pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_recive_correct_answer(browser, num):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{num}/step/1/"
    browser.get(link)
    browser.implicitly_wait(10)
    input = browser.find_element(By.CLASS_NAME, "ember-text-area")
    input.send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    text = message.text
    assert "Correct!" in text, f"Wrong message, got '{text}' instead of 'Correct!'"
