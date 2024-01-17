from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# 1) Count No 0f Rows & Columns
noOfRows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfColumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noOfRows)
print(noOfColumns)

# 2) Read Specific row & Column data - Master in
data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

# 3) Read all the rows and columns data
print("Printing all the rows and columns data")

for r in range(2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='          ')
    print()
# 4) Read data Based on Condition(list books name whose author is Mukesh)
for r in range(2,noOfRows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == 'Mukesh':
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName,"      ",authorName,"       ",price)

driver.quit()