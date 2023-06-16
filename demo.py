import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
# ---chrome

Service_obj= Service ("C:/Users/PoonamSShetty/Documents/chromedriver.exe")

driver = webdriver.Chrome(service=Service_obj)

driver.get("https://rahulshettyacademy.com/client")

driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("vindya.sanil@gmail.com")

driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Aa1234567!")

driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Aa1234567!")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# another way using text...it is only possible in XPATH

driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(4)