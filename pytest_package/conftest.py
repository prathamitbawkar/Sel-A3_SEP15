import time
import pytest
from selenium import webdriver

@pytest.fixture(scope='class',params=['chrome','firefox','edge'])
def setup(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    if parameter == 'firefox':
        driver = webdriver.Firefox()
    if parameter == 'edge':
        driver = webdriver.Edge()

    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

