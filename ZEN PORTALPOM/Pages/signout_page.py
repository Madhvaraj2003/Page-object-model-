# Imported required modules
from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Signout_Page(BasePage):
# Element locators for sign-out     
    profile_icon = (By.XPATH, "//img[contains(@class, 'avatar_banner')]")
    sign_out = (By.XPATH, "//div[text() = 'Sign Out']")

    def signout(self):
# Performs the signout action        
        self.click_element(self.profile_icon)
        self.click_element(self.sign_out)
