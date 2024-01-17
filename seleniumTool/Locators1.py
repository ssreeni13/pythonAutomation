from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# id and name locators
#driver.find_element(By.ID,'small-searchterms').send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_elemenet(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# linktext & partial linktext
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

driver.close() #one browser
driver.quit()  #all_browser

