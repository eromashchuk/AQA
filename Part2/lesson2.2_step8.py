from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

#to fill form
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Imya")
    l_name = browser.find_element(By.NAME, "lastname")
    l_name.send_keys("Familia")   
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email@email.ru")   
#to send email
    file_button = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, "text.txt")           # добавляем к этому пути имя файла 
    file_button.send_keys(file_path)
#to push button
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
    


#element.send_keys(file_path)