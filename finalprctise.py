from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager



service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#a[href*='shop']->css 
#//a[contains(@href,'shop)]
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    productName=product.find_element(By.XPATH,"div/h4/a").text
    if productName=="Blackberry":
        product.find_element(By.XPATH,"div/button").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(4)
successText=driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in  successText
driver.close()






                                




