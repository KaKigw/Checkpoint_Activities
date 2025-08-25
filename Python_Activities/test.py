from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



service = Service(executable_path="Intro/Python_Activities/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/maps")

input_element = driver.find_element(By.CLASS_NAME,"NhWQq")
input_element.send_keys("GOMYCODE" + Keys.ENTER)


time.sleep(60)

driver.quit()