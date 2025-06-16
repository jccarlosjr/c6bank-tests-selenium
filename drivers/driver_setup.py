from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def init_chromedriver(chromedriver_path):
    """
    Initialize Selenium Chrome Webdriver.
    :param chromedriver_path: path to chromedriver.
    :return: Selenium driver instance.
    """
    chrome_service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver
