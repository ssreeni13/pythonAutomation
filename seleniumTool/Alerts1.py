from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

# opens alert windows
driver.find_element(By.XPATH,"//input[@value='Login']").click()  #Login button
time.sleep(5)
driver.switch_to.alert.accept()

driver.close()