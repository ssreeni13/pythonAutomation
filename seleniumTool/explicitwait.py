from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
# mywait = WebDriverWait(driver,10)   #Explicit wait declaration
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotSelectableException,
                                                      Exception]
                       )

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()

searchlinks = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlinks.click()

driver.quit()