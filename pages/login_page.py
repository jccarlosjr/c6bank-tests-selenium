from selenium.webdriver.common.by import By
from utils.utils import alert_confirm, load_icon


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_input = (By.ID, "EUsuario_CAMPO")
        self.pass_input = (By.ID, "ESenha_CAMPO")
        self.login_btn = (By.ID, "lnkEntrar")

    def access(self, url):
        self.driver.get(url)

    def login(self, user, password):
        self.driver.find_element(*self.user_input).send_keys(user)
        self.driver.find_element(*self.pass_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        alert_confirm(self.driver)
        load_icon(self.driver)
        is_logged_in = self.is_logged_in()
        if not is_logged_in:
            raise Exception("Login failed, check your credentials or the login page structure.")

    def is_logged_in(self):
        try:
            self.driver.find_element(By.ID, "lnkSair")
            return True
        except:
            return False
