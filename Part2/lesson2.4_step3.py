# Открыть страницу http://suninjuly.github.io/wait1.html
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

# Нажать на кнопку "Verify"
    time.sleep(3)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

finally:

# Проверить, что появилась надпись "Verification was successful!"
    assert "successful" in message.text
    browser.quit()
