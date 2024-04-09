import pytest
from helpers.user import User
from config import Config
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def new_user():
    return User.create(new_user=True)


@pytest.fixture
def registered_user():
    return User.create(new_user=False)
