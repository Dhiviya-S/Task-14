# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains locators and methods to interact with locators.
class LoginPage(BasePage):


    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Email and password box locator using CSS_SELECTOR
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Enter your mail"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Enter your password "]')

    # Signin Button locator using XPATH
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    # After Signing login page enters into Dashboard page. To assert that 'Dashboard' locator is used.
    DASHBOARD=(By.XPATH,'//p[text()="Dashboard"]')

    # A Popup appears after login so to find and close the pop-up 'DASHBOARD_POPUP' is used
    DASHBOARD_POPUP=(By.XPATH,'//button[@class="custom-close-button"]')

    # LOGOUT appears under profile icon which contains 3 items so both profile_icon and logout_button is used.
    PROFILE_ICON=(By.XPATH,'//img[@id="profile-click-icon"]')
    LOGOUT_BUTTON=(By.XPATH,'//div[contains(text(),"Log out")]')



    # METHODS TO INTERACT WITH THE ELEMENTS
    # login() is used to find username and password and enter the valid data and to click signin button
    def login(self, username, password):

        # self.USERNAME_INPUT,self.PASSWORD_INPUT are locators. username,password are the text to be entered.
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)

        #Clicks the login button after locating the self.LOGIN_BUTTON
        self.click_element(self.LOGIN_BUTTON)
        # After login, the url of the page should change from login to dashboard so locating it using self.DASHBOARD
        self.find_element(self.DASHBOARD)


    # input_displayed is used to validate the email and password box is visible or not
    def input_displayed(self):

        # Locates email and password input box using find_element()
        username_element = self.find_element(self.USERNAME_INPUT)
        password_element = self.find_element(self.PASSWORD_INPUT)

        # Returns the email and password input box is visible or not using is_displayed()
        return username_element.is_displayed() and  password_element.is_displayed()


    # To validate sign_in button is clickable and visible or not
    def signin_button_enabled(self):

        # Locates Sign_in button using find_element() and self.LOGIN_BUTTON is the locator
        signin=self.find_element(self.LOGIN_BUTTON)
        # Returns sign_in button is visible or not using is_displayed() and clickable or not using is_enabled()
        return signin.is_enabled() and signin.is_displayed()


    # To click logout under profile icon and move back to login page
    def logout(self):

        # To close the popup that appears always,using self.DASHBOARD_POPUP
        self.click_element(self.DASHBOARD_POPUP)

        # Logout icon appears under profile icon
        self.click_element(self.PROFILE_ICON)
        self.click_element(self.LOGOUT_BUTTON)

        # After clicking logout, to assert the url changed from dashboard to login
        self.find_element(self.LOGIN_BUTTON)

