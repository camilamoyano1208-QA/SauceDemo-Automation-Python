from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Cartpage (BasePage):
    CHECKOUT_BUTTON= (By.ID, "checkout")

    def start_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)