from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.select import Select




 #For by keyword import package#
from selenium.webdriver.common.by import By

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")

#ID,XPATH,CSSselector,Classname,name,linkText

driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Poonam")
# driver.find_element(By.CSS_SELECTOR,"#inLineRadio1").click()

#Static Dropdown

dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH,"//input[@value='Submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)


time.sleep(50)


