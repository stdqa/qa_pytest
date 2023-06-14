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