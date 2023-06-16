from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
import pytest
from Baseclass import BaseClass



class TestOne(BaseClass):

   def test_e2(self):
    

    self.find_element_by_css_selector("a[href*='shop']").click()
    products=self.find_elements_by_xpath("//div[@class='card h-100']")
    for product in products:
       productName=product.find_element(By.XPATH,"div/h4/a").text
    if productName=="Blackberry":
        product.find_element(By.XPATH,"div/button").click()
    time.sleep(4)

    self.find_element_by_css_selector("a[class*='btn-primary']").click()
    self.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    self.find_element(By.ID,"country").send_keys("ind")
    wait=WebDriverWait(self.driver,10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
    self.find_element(By.LINK_TEXT,"India").click()
    self.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
    self.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    time.sleep(4)
    successText=self.driver.find_element(By.CLASS_NAME,"alert-success").text
    assert "Success! Thank you!" in  successText
    

