from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2023") #mm/dd/yyyy

year = "2023"
month = "March"
date = "30"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next Arrow
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #Previous Arrow - Old State

#Select date
dates = driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break