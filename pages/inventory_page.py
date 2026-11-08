"""Page Object da listagem de produtos (inventário)."""
from selenium.webdriver.common.by import By

from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self):
        return self.text_of(self.TITLE) == "Products"

    def item_count(self):
        return len(self.driver.find_elements(*self.ITEMS))

    def add_first_item_to_cart(self):
        button = self.driver.find_element(
            By.CSS_SELECTOR, ".inventory_item button"
        )
        button.click()

    def cart_count(self):
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)
