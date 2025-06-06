# Imported required modules
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
# Element locators for email, password, login button     
    USERNAME_INPUT = (By.ID,"email")
    PASSWORD_INPUT = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-btn")
    
    def login(self, email, password):
 # Performs login actions       
        self.enter_text(self.USERNAME_INPUT,email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

        
       