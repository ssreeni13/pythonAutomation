from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    #download files in desired location
    preferences = { "download.default_directory":location,"plugins.always_open_pdf_externally":True}
    # # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # # driver = webdriver.Chrome(service=serv_obj)
    chrome_options.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def edge_setup():
    from selenium.webdriver.chrome.service import Service
    edge_options = webdriver.EdgeOptions()
    edge_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    #download files in desired location
    preferences = { "download.default_directory":location,"plugins.always_open_pdf_externally":True}
    # # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # # driver = webdriver.Chrome(service=serv_obj)
    edge_options.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(options=edge_options)
    return driver

def firefox_setup():
    from selenium.webdriver.chrome.service import Service
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    #Settings download files in desired location
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_options.set_preference("browser.download.folderList", 2) #0-desktop 1-downloads folder  2-Desired Location
    firefox_options.set_preference("browser.download.dir", location)
    firefox_options.set_preference("pdfjs.disabled", True) #For Pdf
    # # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
    # # driver = webdriver.Chrome(service=serv_obj)
    driver = webdriver.Firefox(options=firefox_options)
    return driver

driver = chrome_setup()
driver = edge_setup()
driver = firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()