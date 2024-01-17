from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use a raw string or double backslashes in the path

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
# # serv_obj = Service(r"C:\Drivers\chrome-win64\chrome.exe")
# # driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)


driver.get("http://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()


min_slider = driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider = driver.find_element(By.ID,"//body//div//span[2]")
act.drag_and_drop(rome_ele,italy_ele).perform()

print("Location of Sliders Before Moving........")
print(min_slider.location)
print(max_slider.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("Location of Sliders After Moving........")
print(min_slider.location)  # { 'x':158, 'y':252 }
print(max_slider.location)  # { 'x':598, 'y':252 }

driver.close()



