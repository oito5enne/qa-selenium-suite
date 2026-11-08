"""Testes de autenticação — caminho feliz e cenários negativos."""
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


@pytest.mark.smoke
def test_login_valido(driver):
    LoginPage(driver).login(VALID_USER, VALID_PASS)
    assert InventoryPage(driver).is_loaded()


@pytest.mark.regression
@pytest.mark.parametrize(
    "user,password,esperado",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "senha_errada", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_login_invalido(driver, user, password, esperado):
    login = LoginPage(driver)
    login.login(user, password)
    assert esperado.lower() in login.error_message().lower()
