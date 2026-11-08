"""Classe base para todos os Page Objects.

Reúne as interações comuns (esperar, clicar, digitar, ler texto) com
esperas explícitas, evitando sleeps fixos e deixando os testes estáveis.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self._clickable(locator).click()

    def type(self, locator, text):
        field = self._visible(locator)
        field.clear()
        field.send_keys(text)

    def text_of(self, locator):
        return self._visible(locator).text

    def is_visible(self, locator):
        try:
            self._visible(locator)
            return True
        except Exception:
            return False
