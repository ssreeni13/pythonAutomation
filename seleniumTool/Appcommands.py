from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)



driver.close()