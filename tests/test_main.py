import pytest
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestMain:
    # Работают переходы к разделам:«Булки»,«Соусы»,«Начинки».
    @pytest.mark.parametrize(
        "prev, target",
        [
            [locators.MainPage.builder_sauce_tab, locators.MainPage.builder_bread_tab],
            [locators.MainPage.builder_topping_tab, locators.MainPage.builder_sauce_tab],
            [locators.MainPage.builder_bread_tab, locators.MainPage.builder_topping_tab]
        ]
    )
    def test_goto_burger_ingredients_goes_over(self, prev, target, driver, registered_user):
        # переходим с главной страницы на форму логина
        driver.find_element(*locators.MainPage.enter_to_profile_btn).click()

        # заполняем поля, входим, ждем загрузку
        driver.find_element(*locators.Login.email_input).send_keys(registered_user.email)
        driver.find_element(*locators.Login.password_input).send_keys(registered_user.password)
        driver.find_element(*locators.Login.login_btn).click()
        WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(locators.MainPage.make_an_order_btn))

        # клик по prev-заголовку раздела ингредиентов
        # через запуск скрипта т.к. click() по активному заголоку вызызвает ошибку
        prev_element = driver.find_element(*prev)
        driver.execute_script("arguments[0].click();", prev_element)

        # сохраняем класс элемента до и после клика по target-заголовку раздела ингредиентов
        target_element = driver.find_element(*target)
        old_class = target_element.find_element(By.XPATH, "..").get_attribute('class')
        target_element.click()
        new_class = target_element.find_element(By.XPATH, "..").get_attribute('class')

        # проверяем что выбранный заголовок поменял стиль
        assert (('tab_tab_type_current__2BEPc' not in old_class)
                and ('tab_tab_type_current__2BEPc' in new_class))
