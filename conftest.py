import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# @pytest.fixture(scope='class')
# def setup():
#     print(" I will be executing first")
#     yield
#     print(" I will be executed last")


# @pytest.fixture()
# def dataLoad():
#     print("User profile data is being created")
#     return ["Rahul","shetty","rahulshettyacademy.com"]


# @pytest.fixture(params=[("chrome","rahul","shetty"),("Firefox","shetty"),("IE","ss")])
# def crossBrowser(request):
#     return request.param

@pytest.fixture(scope="class")
def setup(request):
    service_obj=Service("C:\poonam\pythonpractise\chromedriver.exe")
    driver=webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver=driver
    yield


