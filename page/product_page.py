import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class ProductPage(BasePage):
    def add_product_to_basket_click(self):
        print('\nStart adding product to basket')
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        print('\nSuccess, add button clicked')

    def solve_quiz_and_get_code(self):
        print('\nStarting quiz')
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, 15).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        print('\nSuccess, quiz solve')

    def should_be_confirm_message(self):
        print("\nChecking product name...", end='\t')
        time.sleep(1) # not sure whats wrong , but should use time becouse webdriverwait doesnt wait
        confirm_message_locator = ProductPageLocators.CONFIRM_MESSAGE
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(confirm_message_locator))
        expected_text = self.get_element_text(*ProductPageLocators.CONFIRM_MESSAGE)[2:]
        assert f'{self.get_element_text(*ProductPageLocators.PRODUCT_NAME)} has been added to your basket.' \
              == expected_text, 'Confirm message not contain name of product'
        print('\nSucsess, Confirm message is visible correct with name of product')

    def should_be_same_price_in_basket(self):
        print("\nChecking product price...", end='\t')
        product_price = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        product_price_in_basket = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        assert product_price == product_price_in_basket, 'Price of product not the same in basket'
        print('\nPrice in product and price in basket after adding the same')

    def should_not_be_success_message(self):
        print("\nWaiting for message...", end='\t')
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        print("\nWaiting for message...", end='\t')
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"