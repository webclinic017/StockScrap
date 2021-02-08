# Import selenium and get PATH for chromedriver.exe, initialize driver, give access to enter key, esc key.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Import action chains
from selenium.webdriver.common.action_chains import ActionChains

# Imports selenium wait until expected_conditions required modules.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

# Imports selenium errors and exceptions.
from selenium.common.exceptions import *

# Imports selenium logger, to disable logging on selenium
import logging
from selenium.webdriver.remote.remote_connection import LOGGER


class WebDriver:        
    '''
    Creates Selenium WebDriver object
    '''
    def __init__(self, PATH='C:\Program Files (x86)\chromedriver.exe', ignore_errors=True):
        self.PATH = PATH
        self.ignore_errors = ignore_errors
    

    def driver(self):
        '''
        Initialize Selenium WebDriver
        # returns Selenium WebDriver
        '''
        # Remove logging
        if self.ignore_errors == True:
            options = webdriver.ChromeOptions()
            options.add_argument("--test-type")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')

            return webdriver.Chrome(self.PATH, chrome_options=options)

        else: 
            
            return webdriver.Chrome(self.PATH)
