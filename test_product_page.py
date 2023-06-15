import pytest
import time
from .page.product_page import ProductPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
#@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i=='7', reason='Server working not correctly')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser):#, promo_offer):
    #link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2' #{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_click()
    page.solve_quiz_and_get_code()
    page.should_be_confirm_message()
    page.should_be_same_price_in_basket()


@pytest.mark.need_review
@pytest.mark.start
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_to_buy()
    basket_page.should_be_message_basket_is_empty()


@pytest.mark.xfail
@pytest.mark.negative_checks
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_click()
    page.should_not_be_success_message()


@pytest.mark.negative_checks
def test_guest_cant_see_success_message(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.negative_checks
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_click()
    page.should_disappear_success_message()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f'http://selenium1py.pythonanywhere.com'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.register_new_user(email=str(time.time()) + "@fakemail.org", password='Qwesdc234c21x2Qweq')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    # @pytest.mark.parametrize('promo_offer',
    #                          [pytest.param(i, marks=pytest.mark.xfail(i == '7', reason='Server working not correctly'))
    #                           for i in range(10)])
    def test_user_can_add_product_to_basket(self, browser):
        # link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_click()
        #page.solve_quiz_and_get_code()
        page.should_be_confirm_message()
        page.should_be_same_price_in_basket()

    @pytest.mark.xfail
    @pytest.mark.negative_checks
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_click()
        page.should_not_be_success_message()
