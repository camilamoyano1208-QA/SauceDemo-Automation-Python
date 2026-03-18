from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME=(By.ID,"first-name")
    LAST_NAME=(By.ID,"last-name")
    POSTAL_CODE=(By.ID,"postal-code")
    CONTINUE_BUTTON=(By.ID,"continue")
    FINISH_BUTTON=(By.ID,"finish")
    SUCCESS_MESSAGE=(By.CLASS_NAME,"complete-header")
    
    
    def fill_checkout_info(self, name, last, zip_code):
        self.type_text(self.FIRST_NAME, name)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.POSTAL_CODE, zip_code)
        self.click_element(self.CONTINUE_BUTTON)

    def finish_purchase(self):
        self.click_element(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
