import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso (driver):
    login= LoginPage(driver)   #se instancia las paginas que se usaran 
    inventory= InventoryPage(driver)

    login.visit("https://www.saucedemo.com/") #abre la web

    login.login_to_sauce("standard_user", "secret_sauce") #realiza el login

    assert inventory.get_title_text()== "Products"    #verificacion
    assert "inventory.html" in driver.current_url

def test_login_fail(driver):
    login= LoginPage(driver)
    login.visit("https://www.saucedemo.com/")

    login.login_to_sauce("usuario_falso", "clave_falsa") #datos falsos

    error_texto= login.get_error_message ()
    assert "Username and password do not match" in error_texto