import pytest
import random
from selenium import webdriver

__base_url = "https://stellarburgers.nomoreparties.site/"

class User():
    prefix = 'sytnik7'

    def __init__(self, new_user = True):
        if new_user:
            suffix = random.randint(100, 999)
            self.username = f'{self.prefix}{suffix}'
            self.email = f'{self.prefix}{suffix}@yandex.ru'
            self.password = f'{random.randint(100000, 999999)}'
        else:
            self.username = f'{self.prefix}000'
            self.email = f'{self.prefix}000@yandex.ru'
            self.password = '111111'

@pytest.fixture
def url():
    return __base_url

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(__base_url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    return User(new_user=True)

@pytest.fixture
def registered_user():
    return User(new_user=False)