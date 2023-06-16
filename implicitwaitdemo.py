
from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
# driver.maximize_window()
#5 seconds is max time out..2 second,3 second
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)
results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
# print(count)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()  

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() 
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)





