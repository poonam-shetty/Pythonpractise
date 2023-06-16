from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--starts-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-error")
service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=chrome_options)


driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
