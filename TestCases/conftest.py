"""
This file contains a setup fixture which will return the driver object
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Utilities import readProperties as read


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    _testUrl = read.readConfigData('appConfig', 'testURL')
    driver.get(_testUrl)
    request.cls.driver = driver

    yield
    driver.quit()
