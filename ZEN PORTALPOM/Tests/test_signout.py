# Imported all the required modules
# Performing pytest
import pytest
from Pages.login_page import LoginPage
from Pages.signout_page import Signout_Page
# uses setup fixture
@pytest.mark.usefixtures("setup")
class TestSignout:
    def test_sign_out(self):
# Performs the Sign-out action        
        login_page = LoginPage(self.driver)       
        logout_page = Signout_Page(self.driver)
        login_page.login("**********mail.com", "**********@2003")
        logout_page.signout()
       
         
