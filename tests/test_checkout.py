"""Teste end-to-end: do login à confirmação de compra."""
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CartPage, CheckoutPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.mark.regression
def test_fluxo_completo_de_compra(driver):
    # Login
    LoginPage(driver).login(VALID_USER, VALID_PASS)

    # Adiciona um item e vai ao carrinho
    inventory = InventoryPage(driver)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    # Confere o carrinho e inicia o checkout
    cart = CartPage(driver)
    assert cart.item_count() == 1
    cart.checkout()

    # Preenche dados e finaliza
    checkout = CheckoutPage(driver)
    checkout.fill_info("Paulo", "Viana", "58000-000")
    checkout.finish()

    assert "Thank you" in checkout.confirmation_text()
