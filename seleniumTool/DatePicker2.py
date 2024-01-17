from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()


# Date of Birth

driver.find_element(By.XPATH, "//input[@id='dob']").click()  #Opens Date Picker

datepicker_month = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_year = Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("1990")

# Select date
alldates = driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text == '25':
        date.click()
        break