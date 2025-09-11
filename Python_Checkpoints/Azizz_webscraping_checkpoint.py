import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

url = 'https://www.aziza.tn/'
page = requests.get(url)
doc = BeautifulSoup(page.text, "html.parser")
if page.status_code == 200:
    body_div_content = doc.find(class_="ng-star-inserted")
    