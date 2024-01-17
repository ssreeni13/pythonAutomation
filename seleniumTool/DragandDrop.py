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


driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

# Mouse Drag and Drop
act = ActionChains(driver)


rome_ele = driver.find_element(By.ID,"box6")
italy_ele = driver.find_element(By.ID,"box106")
act.drag_and_drop(rome_ele,italy_ele).perform()

wsh_ele = driver.find_element(By.ID,"box3")
italy_ele = driver.find_element(By.ID,"box103")
act.drag_and_drop(wsh_ele,italy_ele).perform()


driver.close()



