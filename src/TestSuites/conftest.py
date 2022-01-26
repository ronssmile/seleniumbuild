import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverInfo:



    STAGE_BASE_URL = "https://www.innovuze.com/"
    PROD_BASE_URL = "https://www.coilcraft.com/en-use/tools/"

    base_url = " "
    browser = " "
    environment = " "

#Instantiate Class DriverInfo

driver_info = DriverInfo

def pytest_addoption(parser):
    '''Add parameters when running the program. 

        +Parameters:
            * --env : Environment of the page chosen. Either stage or prod(Production).
            * --browser : Browser used for testing. Chrome, Firefox, or Edge.
        +How to use:
            When running the program, use this in the terminal.
            * pytest --env prod (when you want to test on the production environement. You can leave it blank since default is stage.)
            * pytest --browser firefox (when you want to test using the firefox browser. You can leave it blank since default is chrome.)
    '''
    parser.addoption("--env", action="store", default="stage")
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def getEnv(request):
    '''Add environment fixtures from addoption to your driver.
    Will also add the value of --env to class DriverInfo.environment
    * return: value of --env (stage , prod)
    '''
    _env = request.config.getoption("--env")
    driver_info.environment = _env
    return _env

@pytest.fixture
def getBrowser(request):
    '''Add browser fixtures from addoption to your driver.
    Will also add the value of --browser to class DriverInfo.browser
    * return: value of --browser (chrome , firefox, edge)
    '''
    _browser = request.config.getoption("--browser")
    driver_info.browser = _browser
    return _browser

def init_url(env):
    '''Get the value of --env and add it to class DriverInfo.base_url.
    * return: Base url depends on the value of --env
    '''
    if env == "stage":
        driver_info.base_url = driver_info.STAGE_BASE_URL
        return driver_info.base_url
    elif env == "prod":
        driver_info.base_url = driver_info.PROD_BASE_URL
        return driver_info.base_url

@pytest.fixture
def init_driver(request, getEnv, getBrowser):
    '''Start and initialize the webdriver.
    + Will use the pytest fixtures during the initialization. (All from fixtures with "request")
    + You can edit the options/config to be used in the browser here.(headless, window-size, etc)
    '''

    _url = init_url(getEnv)
    #Set driver options
    if getBrowser == "chrome":

        """You can change/add options for the browser here."""
        options = Options()
        options.headless = True
        # options.add_argument("window-size=1920x1080")

        #Add this if a specific website is very slow, hence it downloads many libraries, images and plugins. {normal, eager(interactive), none}
        c_caps = DesiredCapabilities().CHROME.copy()
        c_caps["pageLoadStrategy"] = "eager" 

        web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=c_caps)
        web_driver.maximize_window()
        web_driver.get(_url)

    elif getBrowser == "firefox":

        """You can change/add options for the browser here."""
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        # options.add_argument("--width=1080")
        # options.add_argument("--height=1920")

        #Add this if a specific website is very slow, hence it downloads many libraries and plugins. {normal, eager(interactive), none}
        ff_caps = DesiredCapabilities().FIREFOX.copy()
        ff_caps["pageLoadStrategy"] = "none" 

        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options, desired_capabilities=ff_caps)
        web_driver.maximize_window()
        web_driver.get(_url)

    #Go/run driver
    request.cls.driver = web_driver
    yield
    web_driver.close()