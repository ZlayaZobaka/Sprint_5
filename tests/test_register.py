import pytest
import locators
from config import Config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestRegister:
    # Успешная регистрация
    def test_register_fill_data_user_created(self, driver, new_user):
        # по ссылкам переходим с главной страницы на форму регистрации
        driver.find_element(*locators.MainPage.header_profile_btn).click()
        driver.find_element(*locators.Login.register_link).click()

        # регистрируемся
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Register.register_btn))
        driver.find_element(*locators.Register.name_input).send_keys(new_user.username)
        driver.find_element(*locators.Register.email_input).send_keys(new_user.email)
        driver.find_element(*locators.Register.pass_input).send_keys(new_user.password)
        driver.find_element(*locators.Register.register_btn).click()

        # ждем появление ссылки Зарегистрироваться и проверяем текущий url
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Login.register_link))
        assert driver.current_url == f'{Config.BASE_URL}login'

    # Ошибка для некорректного пароля
    def test_register_short_password_show_error_msg(self, driver, new_user):
        # по ссылкам переходим с главной страницы на форму регистрации
        driver.find_element(*locators.MainPage.header_profile_btn).click()
        driver.find_element(*locators.Login.register_link).click()

        # регистрируемся с коротким паролем
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Register.register_btn))
        driver.find_element(*locators.Register.name_input).send_keys(new_user.username)
        driver.find_element(*locators.Register.email_input).send_keys(new_user.email)
        driver.find_element(*locators.Register.pass_input).send_keys('12345')
        driver.find_element(*locators.Register.register_btn).click()

        # проверяем, что появилась плашка с текстом Некорректный пароль
        assert driver.find_element(*locators.Register.incorrect_password_msg).is_displayed()
