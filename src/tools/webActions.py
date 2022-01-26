#implicitly wait in seconds
#explictly wait by element actions

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
EC duco = https://selenium-python.readthedocs.io/waits.html

"""

class WebActions:

    """
    Contains Web Interactions.
    """
    def __init__(self,driver):
        self.driver = driver
    
    def web_click(self,by_locator):
        '''Web Interactions: Basic left click on a web element
            ---------------------------------
        
        '''
        
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def web_send_keys(self,by_locator, text):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)    