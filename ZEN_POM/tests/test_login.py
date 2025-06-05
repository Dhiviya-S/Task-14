# Test Classes contains test scripts and calling actions
import pytest
# Importing Class LoginPage from login_page under pages folder
from pages.login_page import LoginPage
# Importing Selenium exceptions to raise when error occurs
from selenium.common.exceptions import TimeoutException



# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogin:


    # test_successful_login() enters valid data and moves into dashboard page
    def test_successful_login(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login("dhiviyainbox01@gmail.com", "$Flowering92")

        # Checks url of the page after login
        assert "https://v2.zenclass.in/dashboard" in self.driver.current_url
        print("Logged in:", self.driver.current_url)


    # test_unsuccessful_login() enters invalid credentials and asserts the url of the page
    def test_unsuccessful_login(self):

        login_page = LoginPage(self.driver)
        login_page.login("dhiviyainbox@gmail.com", "$Flowing9")

        # Checks the url after entering invalid data. This test fails since it cannot enter dashboard page
        assert "https://v2.zenclass.in/dashboard" not in self.driver.current_url, "Invalid Email and Password provided"


    # test_login_exception() enters invalid credentials and raises TimeoutException
    def test_login_exception(self):

        # This test passes since the exception is raised
        with pytest.raises(TimeoutException):
            login_page = LoginPage(self.driver)
            login_page.login("dhiviyainbox@gmail.com", "$Flowing9")


    # test_validate_input_box is used to validate the email and password box is visible or not
    def test_validate_input_box(self):

        # Exception Handling. try block asserts the email and password box is visible or not
        try:
            login_page = LoginPage(self.driver)
            assert login_page.input_displayed()

        # Catches the error and prints the exception
        except Exception as e:
            print(f"Exception:{e}")

        # If no error occurs, else runs
        else:
            print("Username and Password input box is visible and enabled")


    # test_validate_submit() is used to assert the signin button is clickable and visible or not
    def test_validate_submit(self):
        login_page = LoginPage(self.driver)
        assert login_page.signin_button_enabled(),"Signin button is not enabled"


    # test_negative_submit() is used to validate the signin after entering invalid data
    # This test fails after entering invalid data signin button doesn't move to dashboard
    def test_negative_submit(self):
            login_page = LoginPage(self.driver)
            login_page.login("dhiviyainbox@gmail.com", "$Flowing9")
            assert not login_page.signin_button_enabled(),"Submit button enables for valid credentials"


    # test_logout() is used to enter valid data and moves to dashboard page and clicks logout
    def test_logout(self):

        login_page=LoginPage(self.driver)
        login_page.login("dhiviyainbox01@gmail.com", "$Flowering92")

        # Clicks logout icon which appears under profile icon
        login_page.logout()
        # Checks whether logout has been done properly and moved again to login page
        assert "https://v2.zenclass.in/login" in self.driver.current_url
        print("Logged out successfully",self.driver.current_url)


#To generate HTML Report of Pytest cases:pytest -v -s tests/test_login.py --html=report.html
#report.html(to be opened in Browser)



