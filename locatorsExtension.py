from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

 #For by keyword import package#
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//input[@formcontrolname='userEmail']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(10)
