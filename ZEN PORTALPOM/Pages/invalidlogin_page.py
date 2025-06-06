# Imported required Selenium modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class InvalidLogin(BasePage):
    # Locators for page elements (class variable)
    def __init__(self, driver):
        self.driver = driver
    # email input field locator    
    USERNAME_INPUT = (By.ID,"email")
    # password input field locator
    PASSWORD_INPUT = (By.ID,"password")
    # Logout field Locator
    LOGIN_BUTTON = (By.ID,"login-btn")
    # Error message locator
    Error_Message  = (By. XPATH, "//div[@class='invalid-feedback']")
 
    def login(self, email, password):
    # Method to perform invalid login credentials
        self.enter_text(self.USERNAME_INPUT,email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
 
    def get_error_message(self):
        # Method to get error message 
        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.Error_Message))
        return error.text
