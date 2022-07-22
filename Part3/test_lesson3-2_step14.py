import unittest 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)
    f = browser.find_element(By.CSS_SELECTOR, "[action = 'registration_result.html'] > .first_block :nth-child(1) > .form-control.first")
    f.send_keys("Ivan")
    s = browser.find_element(By.CSS_SELECTOR, "[action = 'registration_result.html'] > .first_block :nth-child(2) > .form-control.second")
    s.send_keys("Petrov")
    t = browser.find_element(By.CSS_SELECTOR, "[action = 'registration_result.html'] > .first_block :nth-child(3) > .form-control.third")
    t.send_keys("Smolensk@gmail.com")
    b = browser.find_element(By.CSS_SELECTOR, "button.btn")
    b.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text
    browser.quit()

class TestUnicSelectors(unittest.TestCase):

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(registration(link), "Congratulations! You have successfully registered!")
    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(registration(link), "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()