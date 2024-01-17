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


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)


#Admin ---> User Management ---> Users
admin = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b").click()
usermgmt = driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()
users = driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()

# Mouse Hover
act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()






driver.close()



