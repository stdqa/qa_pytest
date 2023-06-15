from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_to_buy(self):
        print("\nChecking tittle...", end='\t')
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_MESSAGE), \
            "Tittle Items to buy should not be"
        print('Success, basket has no items')

    def should_be_message_basket_is_empty(self):
        print("\nChecking empty message...", end='\t')
        assert "Your basket is empty." in self.get_element_text(*BasketPageLocators.EMPTY_MESSAGE), \
            "Tittle Items to buy should not be"
        print('Success, basket is empty message is visible')
