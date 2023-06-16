from selenium import webdriver
import selenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)
driver.get_screenshot_as_file("screen.png")
