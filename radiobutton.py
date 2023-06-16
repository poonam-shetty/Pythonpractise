
from msilib.schema import RadioButton
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
RadioButton=driver.find_elements(By.XPATH,"//input[@type='radio']")
#print(len(RadioButton))

for radio in RadioButton:
    if radio.get_attribute("value") == "radio2":
        radio.click()

