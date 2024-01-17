from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
# import time
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # driver = webdriver.Chrome(service=serv_obj)
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # driver = webdriver.Chrome(service=serv_obj)
    edge_options.headless = True
    driver = webdriver.Edge(options=edge_options)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # driver = webdriver.Chrome(service=serv_obj)
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    return driver

driver = headless_chrome()
# driver = headless_edge()
# driver = headless_firefox()

driver.get("https://www.demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()

