from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr") #to switch to frame
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Hello")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR ,"h3").text)


