from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# serv_obj = Service("C:\Drivers\chrome-win64\chrome.exe")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Thermax')]/self::a").text
print(text_msg)

# parent
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Thermax')]/parent::td").text
print(text_msg)

# child
childs = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/child::td")
print(len(childs))

# Ancestor
text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr").text
print(text_msg)

# Descendants
descendants = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/descendant::*")
print("No of Descendant Nodes:",len(descendants))

# Following
followings = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/following::*")
print("No of Following Nodes:",len(followings))

# Following-sibiling
followingsiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/following-sibling::*")
print("No of Following-sibiling Nodes:",len(followingsiblings))

# preceding
preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/preceding::*")
print("No of preceding Nodes:",len(preceding))

# preceding-sibling
precedingsiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'Thermax')]/ancestor::tr/preceding-sibling::*")
print("No of preceding-sibling Nodes:",len(precedingsiblings))

driver.close()