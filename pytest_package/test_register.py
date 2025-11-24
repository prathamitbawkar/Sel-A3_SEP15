import time

class TestRegister():
    def test_register(self,setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(5)

    def test_fname(self,setup):
        setup.find_element('xpath', '//input[@id="FirstName"]').send_keys("Prathmesh")
        time.sleep(5)