from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



driver.get("https://rahulshettyacademy.com/")


driver.maximize_window()