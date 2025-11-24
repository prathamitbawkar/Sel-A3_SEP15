import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create driver only once
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)


@pytest.mark.parametrize("username, pwd",[("standard_user", "secret_sauce"),("standard", "secret"),("hihello", "wrongpass")])
def test_login(username, pwd):
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)

    # Enter password
    driver.find_element(By.ID, "password").send_keys(pwd)
    time.sleep(1)

    # Click login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Verification
    if "inventory" in driver.current_url:
        print("Successful login →", username)
    else:
        print("Unsuccessful login →", username)
