# we need to install requests package in settings in python intrepreter
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.deadlinkcity.com/")
driver.maximize_window()

alllinks = driver.find_elements(By.TAG_NAME,'a')
count = 0

for link in alllinks:
    url = link.get_attribute('href')
    try:
      res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")

print("Total No of Broken Links:", count)
