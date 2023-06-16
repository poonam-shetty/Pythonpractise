from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
# to print dynamic content  
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))      

assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=="India"




