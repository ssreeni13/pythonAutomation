from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://admin-demo.nopcommerce.com/register")

emailbox = driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")

print("Result of text:",emailbox.text)  #printed Nothing
print("Result of get_attribute:",emailbox.get_attribute('value'))   #abc@gmailcom

button = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of text:",button.text)
print("Result of get_attribute:",button.get_attribute('value'))

driver.quit()