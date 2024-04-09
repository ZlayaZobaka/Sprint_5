import pytest
import locators
from config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestTransitions:
    # Переход в личный кабинет по клику на «Личный кабинет».
    def test_transition_main_to_profile_profile_opened(self, driver, registered_user):
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

        # ждем появление ссылки Профиль и проверяем текущий url
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.Profile.profile_link))
        assert driver.current_url == f'{Config.BASE_URL}account/profile'

    # Переход из личного кабинета в конструктор по клику на «Конструктор»/логотип Stellar Burgers
    @pytest.mark.parametrize(
        "locator",
        [
            locators.MainPage.header_builder_tab,
            locators.MainPage.header_main_logo_link
        ]
    )
    def test_transition_profile_to_builder_builder_opened(self, locator, driver, registered_user):
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

        # переходим по ссылке из параметра теста
        driver.find_element(*locator).click()

        # ждем появление секции Соберите бургер и проверяем текущий url
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.build_burger_section))
        assert driver.current_url == Config.BASE_URL
