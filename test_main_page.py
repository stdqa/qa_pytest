from .page.main_page import MainPage
from .page.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
<<<<<<< HEAD
    login_page.should_be_login_url()
=======
    login_page.should_be_login_page()
>>>>>>> dc5555fa86511705d5690c31f43308be5f33ef44

def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# def test_url_in_login_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()

def test_should_be_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

