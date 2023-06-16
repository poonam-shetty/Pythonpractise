from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
# action.double_click(driver.find_element(by.))
# action.context_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# time.sleep(5)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()