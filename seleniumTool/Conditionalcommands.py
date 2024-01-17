from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://admin-demo.nopcommerce.com/register")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status:",searchbox.is_displayed())
print("Enabled Status:",searchbox.is_enabled())

rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Default Radio Button Status....")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("After Selecting Male Radio Button Status....")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()

print("After Selecting Female Radio Button Status....")
print(rd_male.is_selected())
print(rd_female.is_selected())

driver.close()