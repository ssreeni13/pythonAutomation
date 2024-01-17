from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use a raw string or double backslashes in the path

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# # driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")   #switch to frame

field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")


# Mouse Double Click
act = ActionChains(driver)

act.double_click(button).perform() #Double Click






driver.close()



