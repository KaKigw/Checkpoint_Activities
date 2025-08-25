import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="Intro/Python_Activities/chromedriver.exe")
driver = webdriver.Chrome(service=service)

def set_search_language (driver, language_code = "en"):
    try:
        language_dropdown = Select(driver.find_element(By.ID,"searchLanguage"))
        language_dropdown.select_by_value(language_code)
    except Exception  as e:
        print(f"Failed to set language '{language_code}': {e}")

def set_search_element (driver,Search_Element):
    input_element = driver.find_element(By.ID,"searchInput")
    input_element.send_keys(Search_Element + Keys.ENTER)




language_choice = input("Choose a language to search with (e.g: en, fr, ar)" ).strip()
Search_Element = input("What do you want to search? ").strip()

driver.get("https://www.wikipedia.org/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID,"searchLanguage"))
    )

set_search_language(driver,language_choice)
set_search_element(driver,Search_Element)



time.sleep(60)
driver.quit()