from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://www.demo.nopcommerce.com/")
driver.maximize_window()

# Capture Cookies from the browser
Cookies = driver.get_cookies()
print("Size of Cookies:", len(Cookies))

# Print details of all cookies
# for c in Cookies:
#     print(c)
#     print(c.get('name'),":",c.get('value'))

# Add new cookies to the browser
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new one:",len(cookies))

# Delete specific cookie from the browser
driver.delete_cookie({"MyCookie"})
cookies = driver.get_cookies()
print("Size of cookies after deleted one:",len(cookies))

# Delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleted all:",len(cookies))