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


driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")


# Mouse Right Click
act = ActionChains(driver)

act.context_click(button).perform() #Right Click

time.sleep(5)

driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click  #copy
time.sleep(3)
driver.switch_to.alert.accept()






driver.close()



