from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

 #For by keyword import package#
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://bix-bytes.greythr.com/uas/portal/auth/login?login_")
driver.find_element(By.ID,"username").send_keys("BBS0120")
driver.find_element(By.ID,"password").send_keys("Poon@22@14")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(10)
