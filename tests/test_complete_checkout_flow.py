from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cartpage
from pages.checkout_page import CheckoutPage


def test_complete_purchase_flow(driver):
    login= LoginPage(driver)
    inventory= InventoryPage (driver)
    cart= Cartpage(driver)
    checkout= CheckoutPage(driver)

    login.open_page()
    login.login_to_sauce("standard_user", "secret_sauce") #ingresar

    inventory.add_backpack_to_cart() #agregar producto y navegar al carrito
    inventory.go_to_cart()

    cart.start_checkout()  #proceso de checkout (carrito-datos-finalizar)
    checkout.fill_checkout_info("Camila", "QA", "E161DB")
    checkout.finish_purchase()

    assert checkout.get_success_message() == "Thank you for your order!"




