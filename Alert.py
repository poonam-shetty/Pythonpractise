from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name= "Rahul"
service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR ,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
time.sleep(5)
alert=driver.switch_to.alert
alertText=alert.text
print(alertText)
assert name in alertText
alert.accept()



