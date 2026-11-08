"""Testes da listagem de produtos e do carrinho."""
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.fixture
def logged_in(driver):
    LoginPage(driver).login(VALID_USER, VALID_PASS)
    return InventoryPage(driver)


@pytest.mark.smoke
def test_inventario_lista_produtos(logged_in):
    assert logged_in.item_count() == 6


@pytest.mark.regression
def test_adicionar_item_ao_carrinho(logged_in):
    assert logged_in.cart_count() == 0
    logged_in.add_first_item_to_cart()
    assert logged_in.cart_count() == 1
