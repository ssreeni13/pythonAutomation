from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use a raw string or double backslashes in the path

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# # driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

# Login
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)


#Admin ---> User Management ---> Users
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()


# Total rows in a table
rows = len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
print("Total Number of Rows in a Table:", rows)

count = 0
for r in range(1,rows+1):
    status = driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr["+str(r)+"]/td[5]").text
    if status == "Enabled":
        count = count + 1

print("Total Number of Users:",rows)
print("Total Number of Enabled Users:",count)
print("Total Number of Disabled Users:",rows-count)




driver.close()



