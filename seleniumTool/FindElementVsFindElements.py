from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demo.nopcommerce.com/")

# 1) Locator matching with single web element
element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("Apple MacBook Pro 13-inch")

# 2) Locator matching with multiple web elements
element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text)

# 3) Element not available then throw NoSuchElementException
login_element = driver.find_element(By.LINK_TEXT,"Log")
login_element.click()

# find_elements() - Returns multiple webElements
# 1) Locator matching with single web element
elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(elements))
elements[0].send_keys("Apple MacBook Pro 13-inch")

# # 2) Locator matching with multiple web elements
elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
print(elements[0].text) #sitemap
for ele in elements:
    print(ele.text)

# 3) Element not available then throw NoSuchElementException
login_element = driver.find_elements(By.LINK_TEXT,"Log")
print("Elements Returned:",len(login_element))

driver.quit()