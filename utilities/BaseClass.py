import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def verify_presence(self, locator):
        wait = WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(locator))
        
        
# checking jenkins integration        
