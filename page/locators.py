from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTR_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTR_EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTR_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTR_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    CONFIRM_MESSAGE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-success  fade in"][1]')
    PRICE_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.XPATH, "//ul[@class='nav navbar-nav navbar-right']/li[1]")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    ITEMS_TO_BUY_MESSAGE = (By.CSS_SELECTOR, ".basket-title h2")
