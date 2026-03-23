from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_bag_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open_page()
    
    # Login directo
    login.login_to_sauce("standard_user", "secret_sauce")

    print(f"\nURL actual después del login: {driver.current_url}")
    
    # Acción: Agregar mochila
    inventory.add_backpack_to_cart()
    
    # Validación
    assert inventory.get_cart_count() == "1"