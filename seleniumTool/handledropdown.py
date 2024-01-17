from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# drpcountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry = Select (driver.find_element(By.XPATH,"//select[@id='input-country']"))

# select option from the dropdown
drpcountry.select_by_visible_text()
drpcountry.select_by_value("10")
drpcountry.select_by_index(13)

# capture all the options and print them
alloptions = drpcountry.options
print("Total no of options:", len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# select option from dropdown without using built-in method
for opt in alloptions:
    if opt.text == 'india':
        opt.click()
        break

allOptions = driver.find_elements(By.XPATH,'//*[id="input-country"]/option')
print(len(allOptions))