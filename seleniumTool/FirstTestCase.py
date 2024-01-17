# My First Test Case
# 1) Open Web Browser(Chrome/Firefox/Edge)
# 2) Open URL  https://opensource-demo.orangehrmlive.com/, https://admin-demo.nopcommerce.com/login
# 3) Enter Username (Admin) (admin@yourstore.com)
# 4) Enter Password (admin123) (admin)
# 5) Click on Login.
# 6) Capture title pof the home page (Actual Title) (Dashboard / nopCommerce administration)
# 7) Verify title of the page: OrangeHRM (Expected) (Dashboard / nopCommerce administration)
# 8) Close Browser

# selenium3
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="C:\Drivers\chrome-win64\chrome.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("username").send_keys("Admin")
# driver.find_element_by_name("password").send_keys("admin123")
# driver.find_element_by_class("oxd-button").click()
#
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
#
# driver.close()

# selenium4
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# # Use a raw string or double backslashes in the path
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# # driver = webdriver.Chrome(service=serv_obj)
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element(By.NAME, "txtUsername").send_keys("Admin")  # Assuming the correct name is "txtUsername"
# driver.find_element(By.NAME, "txtPassword").send_keys("admin123")  # Assuming the correct name is "txtPassword"
# driver.find_element(By.ID, "btnLogin").click()  # Assuming the correct class name is "button"
#
# act_title = driver.title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
#
# driver.close()


# selenium4.1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Use a raw string or double backslashes in the path

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")  # Assuming the correct name is "txtUsername"
driver.find_element(By.NAME, "Password").send_keys("admin")  # Assuming the correct name is "txtPassword"
driver.find_element(By.CLASS_NAME, "login-button").click()  # Assuming the correct class name is "button"

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()



