
from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        

radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton" )
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
time.sleep(10)

assert driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(3)
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(3)
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
        
        
        
        




