import pytest

# @pytest.fixture()
# def greet():
#     print("Good Morning")
#     yield 1
#     print("Good Afternoon")
#
# def test_login(greet):
#     print("Login executing")
#
# def test_signup():           # wont apply fixture as greet is not called
#     print("Signup executing")
#
# def test_logout(greet):
#     print("Logout executing")


@pytest.fixture(scope = 'class') # scope = module for whole file apply only once / autouse = true / scope = class for class level
def setup():
    print("Good morning")
    yield
    print("Good evening")

def test_signup():
    print("Signup executing")

def test_logout():
    print("Logout executing")

class TestSample:
    def test_signup(self):
        print("signup executing")
    def test_login(self):
        print("login executing")
    def test_reg(self):
        print("reg executing")

class TestSpam:
    def test_google(self,setup):
        print("google executing")
    def test_facebook(self):
        print("facebook executing")








