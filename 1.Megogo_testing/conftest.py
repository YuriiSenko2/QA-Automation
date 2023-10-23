from selenium.webdriver import Chrome
from Megogo_testing.pages.megogo_pages import Submenu
from Megogo_testing.pages.megogo_pages import Widgets
from Megogo_testing.pages.megogo_pages import HeaderNav
from Megogo_testing.pages.megogo_pages import SignIn
from Megogo_testing.cookies_and_storage import CookiesManipulations
from Megogo_testing.cookies_and_storage import LocalStorageManipulations
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('HW_20/drivers/chromedriver.exe')
    driver.get('https://megogo.net/ua')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def submenu(driver):
    yield Submenu(driver)


@pytest.fixture
def widgets(driver):
    yield Widgets(driver)


@pytest.fixture
def header_nav(driver):
    yield HeaderNav(driver)


@pytest.fixture
def cookies(driver):
    yield CookiesManipulations(driver)


@pytest.fixture
def local_storage(driver):
    yield LocalStorageManipulations(driver)


@pytest.fixture
def sign_in(driver):
    yield SignIn(driver)