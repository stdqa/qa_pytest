from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url , 'Login link is not presented'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), 'Login form is not presented'
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), 'Registr form is not presented'
        assert True

    def register_new_user(self, email, password):
        print('\nStarting register new user')
        email_field = self.browser.find_element(*LoginPageLocators.REGISTR_EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTR_PASSWORD_FIELD)
        pass_field.send_keys(password)
        conf_pass_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        conf_pass_field.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON)
        submit.click()
        print('\nUser registered')
