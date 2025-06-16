# Imported required modules
# Testing framework  
import pytest
# Page object to test 
from Pages.invalidlogin_page import InvalidLogin

# Using setup fixture
@pytest.mark.usefixtures("setup")
class TestInvalidlogin:
        
    def test_invalid_login(self):
# Tests invalid login (Negative test case)        
        login_page = InvalidLogin(self.driver)
        login_page.login("wrong@mail.com", "wrongpass")
# Attempts to login but shows error message        
        error_text = login_page.get_error_message()
        assert "Incorrect Email or Password" in error_text
       