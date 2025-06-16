# Imported required modules
# Performing pytest
import pytest
from Pages.login_page import LoginPage

# Uses setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestLogin:
# Tests successful login    
    def test_login(self):
# Initialize page object      
        login_page = LoginPage(self.driver)
# Performs login        
        login_page.login("madhva3@gmail.com", "Madhva@2003")
        assert "guvi.in" in self.driver.current_url
      
       


