
import os
import sys
from pathlib import Path

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebClient(object):

    def __init__(self):
        self.driver = None
        self.timeout = 5

    def __getattr__(self, name):
        if hasattr(self.driver, name):
            return getattr(self.driver, name)

    def open(self, driver):
        self.driver = driver

    def wait_element_by_css_selector(self, selector):
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        WebDriverWait(self.driver, self.timeout).until(element_present)


webclient = WebClient()

# TODO: use a config to choose browser
sys.path.append(str(Path(__name__).absolute().parent / 'drivers'))
os.environ['PATH'] = ':'.join(sys.path)

webclient.open(webdriver.Firefox())
