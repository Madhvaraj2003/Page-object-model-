# Imported required modules
# Testing frame work
import pytest
from selenium import webdriver

# Fixtures that runs once per test class
@pytest.fixture(scope="class")
# Gives access to the requesting test context and sets up and tears down the webdriver for test classes
def setup(request):
# Creates chrome webdriver instance    
    driver = webdriver.Chrome()  
# Opens the login page    
    driver.get("https://www.guvi.in/sign-in/")
# Maximizes window    
    driver.maximize_window()
# Makes driver avilable to the classes    
    request.cls.driver = driver
# Execution passes here until tests complete
    yield
# Closes the browser after finishung the test
    driver.quit()

  