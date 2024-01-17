from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@class='uprcse semi-bold']").click()
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys("C:\SeleniumPractice\sample.pdf")
