# import time
import pytest
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# # Create driver only once
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 10)
#
# driver.get("https://www.saucedemo.com/")
# time.sleep(1)
#
# @pytest.mark.dependency()
# def test_login():
#     driver.find_element('id','user-name').send_keys("standard_user")
#     time.sleep(2)
#     driver.find_element('id','password').send_keys("secret_sauce")
#     time.sleep(2)
#     driver.find_element('id','login-button').click()
#     time.sleep(2)
#     wait_.until(expected_conditions.url_contains("inventory"))
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout():
#     driver.find_element('id','react-burger-menu-btn').click()
#     time.sleep(2)
#     driver.find_element('id','logout_sidebar_link').click()


class TestSample:
    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")

    @pytest.mark.dependency(depends=["TestSample::test_login"])
    def test_logout(self):
        print("logout executing")