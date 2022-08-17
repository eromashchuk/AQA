import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_guest_should_add_item_to_basket(browser):
    browser.get(link)
    x = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(30) #на всякий случай, а то спорят в комментах
    assert x, 'Items not found or button unavailiable'

