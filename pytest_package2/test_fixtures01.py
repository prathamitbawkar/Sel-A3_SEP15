import time
import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://testautomationpractice.blogspot.com/")
    time.sleep(2)
    yield driver

class TestRegister:
    def test_reg(self,setup):
        setup.find_element('xpath', '//input[@placeholder="Enter Name"]').send_keys('Prathmesh M')
        time.sleep(2)
    def test_sendemail(self,setup):
        setup.find_element('xpath', '//input[@placeholder="Enter EMail"]').send_keys('pratz@gmail.com')
        time.sleep(2)
    # driver.find_element('xpath', '//input[@placeholder="Enter Phone"]').send_keys('9876543210')
    # time.sleep(2)
    # driver.find_element('xpath', '//input[@class="form-control"]').send_keys('Park street,mumbai')
    # time.sleep(2)
    # driver.find_element('xpath', '//input[@id="male"]]').click()
    # time.sleep(2)


