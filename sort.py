from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


browserSortedVeggies=[]
service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

#click on column header

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

#collect all veggie names-BrowserSortedveggieList(A,B,C)
veggieWebElements=driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)


originalBrowserSortedList=browserSortedVeggies.copy()
time.sleep(4)


#Sort this BrowserSortedveggieList=> newSortedList->(A,B,C)
browserSortedVeggies.sort()

assert browserSortedVeggies==originalBrowserSortedList