import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# import time
import XLUtils


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\\Users\\Sreenivas Sreeni\\Documents\\Book2.xlsx"
rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    # reading data from excel
    price = XLUtils.readData(file,"Sheet1",r,1)
    roi = XLUtils.readData(file, "Sheet1", r, 2)
    per1 = XLUtils.readData(file, "Sheet1", r, 3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    freq = XLUtils.readData(file,"Sheet1",r,5)
    exp_value = XLUtils.readData(file, "Sheet1", r, 6)

    #passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(price)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    freqdrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    freqdrp.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click() #calculate button

    act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    #validation
    if float(exp_value) == float(act_value):
        print("Test Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()