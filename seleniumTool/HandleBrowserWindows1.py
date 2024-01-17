from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# windowid = driver.current_window_handle
# print(windowid)
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()


# windowid = driver.current_window_handle
# print(windowid)
# windowIDs = driver.window_handles

# Approach 1
# parentwindowid = windowIDs[0]
# childwindowid = windowIDs[1]
#
# driver.switch_to.window(childwindowid)
# print("Title of the child window",driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("Title of the parent window",driver.title)

# Approach 2
# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)
#
# time.sleep(3)
# Close specific browser windows
# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     if driver.title == "OrangeHRM HR Software | Free HR Software | HRMS | HRIS" or driver.title == 'XYZ':
# driver.quit()
