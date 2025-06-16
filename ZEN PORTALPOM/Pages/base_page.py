# Imported required modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Contains coomon methods for all the pages
class BasePage:
# Initializes base page with webdriver    
    def __init__(self, driver):
        self.driver = driver

# Finds a visible element with explicit wait
    def find_element(self,locator, timeout=20):

# Waits for elements to visible        
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

# Clicks an element after waiting for it   
    def click_element(self, locator, timeout=20):
# finds the element first        
        element = self.find_element(locator, timeout)
# Performs click action        
        element.click()

# Enters text into a field after clearing it
    def enter_text(self, locator, text, timeout=20):
# finds the element first        
        element = self.find_element(locator, timeout)
# And clears it        
        element.clear()
        element.send_keys(text)
   
    # def get_current_url(self):
    #     return self.driver.current_url
