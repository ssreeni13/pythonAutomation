from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click(

#Find No of links in a page
# links = driver.find_elements(By.TAG_NAME,'a')
links = driver.find_elements(By.XPATH,'//a')
print("Total no of links:",len(links))

# print all the links
for link in links:
    print(link.text)