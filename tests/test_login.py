import pytest
import locators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной,
    def test_login_from_main_page_logged_on(self, driver, url, registered_user):
        # переходим с главной страницы на форму логина
        driver.find_element(*locators.MainPage.enter_to_profile_btn).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # проверяем, что перешли на url главной страницы
        assert driver.current_url == url

    # Вход через кнопку «Личный кабинет»,
    def test_login_from_profile_btn_logged_on(self, driver, url, registered_user):
        # переходим с главной страницы на форму логина по кнопке Личный кабинет
        driver.find_element(*locators.MainPage.header_profile_btn).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # проверяем, что перешли на url главной страницы
        assert driver.current_url == url

    # Вход через кнопку в форме регистрации,
    def test_login_from_register_form_logged_on(self, driver, url, registered_user):
        # по ссылкам переходим по страницам: главная > логин > регистрация > логин
        driver.find_element(*locators.MainPage.header_profile_btn).click()
        driver.find_element(*locators.Login.register_link).click()
        driver.find_element(*locators.Register.login_link).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # проверяем, что перешли на url главной страницы
        assert driver.current_url == url

    # Вход через кнопку в форме восстановления пароля.
    def test_login_from_forgotten_form_logged_on(self, driver, url, registered_user):
        # по ссылкам переходим по страницам: главная > логин > восстановление > логин
        driver.find_element(*locators.MainPage.header_profile_btn).click()
        driver.find_element(*locators.Login.forgot_pass_link).click()
        driver.find_element(*locators.ForgotPassword.login_link).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # проверяем, что перешли на url главной страницы
        assert driver.current_url == url
