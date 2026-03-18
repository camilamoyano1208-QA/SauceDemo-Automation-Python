from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage (BasePage):
    TITLE= (By.CLASS_NAME,  "title")
    ADD_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    CART_BADGE= (By.CLASS_NAME, "shopping_cart_badge")
    GO_CART=(By.CLASS_NAME, "shopping_cart_link")

    def get_title_text (self):
        return self.get_text (self.TITLE)
    
    def add_backpack_to_cart(self):
        self.click_element(self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click_element(self.GO_CART)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

