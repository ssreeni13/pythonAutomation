from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://www.demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\Sreenivas Sreeni\\PycharmProjects\pythonAutomation\seleniumTool\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

# driver.get_screenshot_as_png() #driver.get_screenshot_as_base64() #saves in binary format

driver.quit()