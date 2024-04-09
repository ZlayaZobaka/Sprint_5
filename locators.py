from selenium.webdriver.common.by import By


# Локаторы главной страницы
class MainPage:
    # кнопка Войти в аккаунт
    enter_to_profile_btn = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # логотип Stellar Burgers
    header_main_logo_link = (By.XPATH, './/div[@class = "AppHeader_header__logo__2D0X2"]')

    # секция Соберите бургер
    build_burger_section = (By.CSS_SELECTOR, '.BurgerIngredients_ingredients__1N8v2')

    # кнопка Оформить заказ
    make_an_order_btn = (By.XPATH, './/button[text() = "Оформить заказ"]')

    # кнопка Личный кабинет в заголовке
    header_profile_btn = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'
                                    '[text() = "Личный Кабинет"]')

    # закладка Конструктор
    header_builder_tab = (By.XPATH, './/p[@class = "AppHeader_header__linkText__3q_va ml-2"]'
                                    '[text() = "Конструктор"]')

    # закладка Булки
    builder_bread_tab = (By.XPATH, './/span[text() = "Булки"]')

    # закладка Соусы
    builder_sauce_tab = (By.XPATH, './/span[text() = "Соусы"]')

    # закладка Начинки
    builder_topping_tab = (By.XPATH, './/span[text() = "Начинки"]')


# Локаторы страницы авторизации
class Login:
    # поле для ввода Email
    email_input = (By.XPATH, './/input[@type = "text"][@name = "name"]')

    # поле для ввода пароля
    password_input = (By.XPATH, './/input[@type = "password"][@name = "Пароль"]')

    # кнопка Войти
    login_btn = (By.CSS_SELECTOR, '.button_button_size_medium__3zxIa')

    # ссылка Зарегистрироваться
    register_link = (By.LINK_TEXT, 'Зарегистрироваться')

    # ссылка Восстановить пароль
    forgot_pass_link = (By.LINK_TEXT, 'Восстановить пароль')


# Локаторы страницы регистрации
class Register:
    # поле для ввода имени пользователя
    name_input = (By.XPATH, './/label[text()="Имя"]/parent::div/input')

    # поле для ввода Email
    email_input = (By.XPATH, './/label[text()="Email"]/parent::div/input')

    # поле для ввода пароля
    pass_input = (By.XPATH, './/input[@type = "password"][@name = "Пароль"]')

    # кнопка Зарегистрироваться
    register_btn = (By.XPATH, './/button[text() = "Зарегистрироваться"]')

    # ссылка Войти
    login_link = (By.LINK_TEXT, 'Войти')

    # сообщение "Некорректный пароль"
    incorrect_password_msg = (By.XPATH, './/p[text()="Некорректный пароль"]')


# Локаторы страницы профиля пользователя
class Profile:
    # имя пользователя
    name_input = (By.XPATH, './/label[text()="Имя"]/parent::div/input')

    # ссылка Профиль
    profile_link = (By.LINK_TEXT, 'Профиль')

    # ссылка Выход
    logoff_btn = (By.XPATH, './/button[text() = "Выход"]')


# Локаторы страницы восстановления пароля
class ForgotPassword:
    # поле для ввода Email
    email_input = (By.XPATH, './/label[text()="Email"]/parent::div/input')

    # кнопка Восстановить
    register_btn = (By.XPATH, './/button[text() = "Восстановить"]')

    # ссылка Войти
    login_link = (By.LINK_TEXT, 'Войти')

# Служебные локаторы
class Common:
    # поиск родителя
    parent = (By.XPATH, "..")