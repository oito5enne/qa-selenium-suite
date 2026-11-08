"""Fixtures compartilhadas do pytest: ciclo de vida do WebDriver.

Centralizar a criação do driver aqui mantém os testes limpos e torna
trivial trocar de navegador ou rodar em modo headless (CI).

O driver é resolvido pelo Selenium Manager (embutido no Selenium 4.6+),
que baixa automaticamente a versão de chromedriver compatível com o
navegador instalado — dispensando gerenciar o driver na mão.
"""
import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")


def _find_browser():
    """Localiza o binário do Chrome/Chromium (CHROME_BIN sobrescreve)."""
    candidates = (
        os.getenv("CHROME_BIN"),
        "chromium", "chromium-browser",
        "google-chrome", "google-chrome-stable",
    )
    for name in candidates:
        if name and shutil.which(name):
            return shutil.which(name)
    return None


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

    browser = _find_browser()
    if browser:
        options.binary_location = browser

    # Selenium Manager baixa o chromedriver certo automaticamente
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    drv.get(BASE_URL)
    yield drv
    drv.quit()
