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

# driver.get("https://www.demo.nopcommerce.com/")
# driver.maximize_window()
# reglink = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

# New Tab - Selenium4 : Opens a new tab and switched to new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.orangehrm.com/")

# New Tab - Selenium4 : Opens a new browser window and switched to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")


driver.quit()