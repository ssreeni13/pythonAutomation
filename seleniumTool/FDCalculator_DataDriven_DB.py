import time
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()


# insert, update, delete
# insert_query = "insert into student values(104,'Kim')"
# update_query = "update student set sname='Mary' where sid=104"
# delete_query = "delete from student where sid=104"

try:
    con = mysql.connector.connect(host="localhost", port=3307, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # Create Cursor
    curs.execute("select * from caldata")  # execute query through cursor

    for row in curs:
        # Reading Data from excel
        price = row[0]
        roi = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_value = row[5]

        #Passing data to the application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(price)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(roi)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)

        freqdrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        freqdrp.select_by_visible_text(freq)
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()  # calculate button

        act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # validation
        if float(exp_value) == float(act_value):
            print("Test Passed")

        else:
            print("Test Failed")
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
    con.close()
except:
    print("Connection Unsuccessful....")

driver.close()