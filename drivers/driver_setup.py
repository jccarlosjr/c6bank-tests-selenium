from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW 
from selenium import webdriver
from config.config import LOCAL_USER_PATH


def init_chromedriver(chromedriver_path):
    """
    Initialize Selenium Chrome Webdriver.
    :param chromedriver_path: path to chromedriver.
    :return: Selenium driver instance.
    """
    chrome_service = Service(chromedriver_path)
    # chrome_service.creation_flags = CREATE_NO_WINDOW
    # options.add_argument(LOCAL_USER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver
