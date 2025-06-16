from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def alert_confirm(driver):
    try:
        wait = WebDriverWait(driver, 1)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass


def load_icon(driver):
    try:
        load = driver.find_element(By.ID, 'ctl00_Image2')
        if load:
            waitload = WebDriverWait(driver, 5)
            waitload.until(EC.invisibility_of_element((By.ID, 'ctl00_Image2')))
    except:
        pass

