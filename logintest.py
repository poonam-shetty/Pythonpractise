from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(5)
driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
time.sleep(5)

driver.find_element(By.NAME,"password").send_keys("learning")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='radio']").click()
time.sleep(5)


dropdown=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
dropdown.select_by_visible_text("Teacher")
# dropdown.select_by_index(0)
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@value='Sign In']").click()
time.sleep(5)




