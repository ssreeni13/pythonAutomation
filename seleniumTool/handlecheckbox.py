from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) Select specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday']").click()

# 2) Select all the checkboxes
checkboxes = driver.find_element(By.XPATH,"//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))

# Approach1
for i in range(len(checkboxes)):
    checkboxes[i].click()

# Approach2
for checkbox in checkboxes:
    checkbox.click()

# Select Multiple Checkbox by Choice
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
    checkbox.click()

# 4)select last 2 checkboxes
# range(5,7) --> 6,7
# totalnoofelements-2 = starting index
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

# 5)select first 2 checkboxes
for i in range(len(checkboxes)):
    if i<2:
         checkboxes[i].click()

# 6) Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
       checkbox.click()

driver.quit()