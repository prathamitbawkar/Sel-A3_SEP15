import time

class TestLogin():
    def test_login(self,setup):
        setup.find_element('xpath', '//a[@class="ico-login"]').click()
        time.sleep(5)

    def test_fname(self,setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys("prathamitbawkar@gmail.com")
        time.sleep(5)