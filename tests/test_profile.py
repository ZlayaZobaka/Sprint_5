import pytest
import locators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestProfile:
    # Работает выход по кнопке «Выйти» в личном кабинете.
    def test_logoff_click_user_logs_out(self, driver, url, registered_user):
        # переходим с главной страницы на форму логина
        driver.find_element(*locators.MainPage.enter_to_profile_btn).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # кликаем по кнопке Личный кабинет
        driver.find_element(*locators.MainPage.header_profile_btn).click()

        # кликаем по ссылке Выход
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Profile.logoff_btn))
        driver.find_element(*locators.Profile.logoff_btn).click()

        # ждем появление ссылки Зарегистрироваться и проверяем текущий url
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Login.register_link))
        assert driver.current_url == f'{url}login'
