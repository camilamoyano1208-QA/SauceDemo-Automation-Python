from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage (BasePage):
    USERNAME_INPUT= (By.ID, "user-name")
    PASSWORD_INPUT= (By.ID, "password")
    LOGIN_BTN= (By.ID,"login-button")
    ERROR_MSG= (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username (self, username): #ACCIONES DE LA PAGINA
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password (self, password):
        self.type_text (self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text (self.ERROR_MSG)

    def login_to_sauce(self, user,pwd):
        self.enter_username (user)
        self.enter_password (pwd)
        self.click_login()