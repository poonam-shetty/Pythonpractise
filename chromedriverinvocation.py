from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
opts=ChromeOptions()
opts.add_experimental_option("detech",True)
driver=Chrome(chrome_options=opts)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()

