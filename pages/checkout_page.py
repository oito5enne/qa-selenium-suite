"""Page Objects do carrinho e do fluxo de checkout."""
from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    def item_count(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def checkout(self):
        self.click(self.CHECKOUT_BTN)


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL, postal)
        self.click(self.CONTINUE_BTN)

    def finish(self):
        self.click(self.FINISH_BTN)

    def confirmation_text(self):
        return self.text_of(self.CONFIRMATION)
