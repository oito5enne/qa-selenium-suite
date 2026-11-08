"""Fixtures compartilhadas do pytest: ciclo de vida do WebDriver.

Centralizar a criação do driver aqui mantém os testes limpos e torna
trivial trocar de navegador ou rodar em modo headless (CI).
"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


@pytest.fixture
def driver():
    """Entrega um WebDriver pronto e garante o encerramento ao fim do teste.

    HEADLESS=1 (padrão em CI) roda sem abrir janela.
    """
    options = Options()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(5)
    drv.get(BASE_URL)
    yield drv
    drv.quit()
