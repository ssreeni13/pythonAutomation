from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use a raw string or double backslashes in the path

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# # driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYoffset;")
# print("Number of pixels moved:",value) #3000

# 2. Scroll down page till the element is visible
# flag = driver.find_element(By.XPATH,"//img@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYoffset;")
# print("Number of pixels moved:",value)

# 3. Scroll down page till end
# driver.execute_script("window.scrollBy(0,document.body.scrollheight)")
# value = driver.execute_script("return window.pageYoffset;")
# print("Number of pixels moved:",value)  #5990.8330078125

# 4. Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollheight)")
value = driver.execute_script("return window.pageYoffset;")
print("Number of pixels moved:",value)


driver.close()



