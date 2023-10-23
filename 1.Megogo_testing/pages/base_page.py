from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Megogo_testing.core.tuple_for_locators import LocatorTuple


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._web_driver_wait = WebDriverWait(self.driver, 10)

    def _wait_until_el_appears_to_click(self, locator: LocatorTuple):
        return self._web_driver_wait.until(EC.presence_of_element_located(locator.to_tuple())).click()

    def _wait_until_el_appears_for_input(self, locator: LocatorTuple, keys):
        send = self._web_driver_wait.until(EC.presence_of_element_located(locator.to_tuple()))
        return send.send_keys(keys, Keys.ENTER)

    def _wait_until_is_clickable(self, locator: LocatorTuple):
        return self._web_driver_wait.until(EC.element_to_be_clickable(locator.to_tuple())).click()


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def retrieve_cookies(self):
        cookie_list = []
        for cookie in self.driver.get_cookies():
            cookie_list.append(cookie)
        return cookie_list

    def get_specific_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def add_cookie(self, key_name, key_value):
        return self.driver.add_cookie({'name': key_name, 'value': key_value})

    def specific_cookie_deletion(self, cookie_name):
        return self.driver.delete_cookie(cookie_name)

    def all_cookies_deletion(self):
        return self.driver.delete_all_cookies()


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def retrieve_local_storage(self):
        storage_list = []
        for elements in self.driver.execute_script("return window.localStorage"):
            storage_list.append(elements)
        return storage_list

    def get_specific_storage_element(self, element_name):
        return self.driver.execute_script(f"return window.localStorage['{element_name}'];")

    def add_element_to_storage(self, el_name, el_value):
        return self.driver.execute_script(f"window.localStorage['{el_name}'] = '{el_value}'")
