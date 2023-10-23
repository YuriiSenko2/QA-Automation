from Megogo_testing.pages.base_page import Cookies
from Megogo_testing.pages.base_page import LocalStorage


class CookiesManipulations(Cookies):
    def __init__(self, driver):
        super().__init__(driver)

    def all_cookies(self):
        for el in self.retrieve_cookies():
            print(el)

    def specific_cookie(self, name):
        cookie_name = f'{name}'
        print(self.get_specific_cookie(cookie_name))

    def new_cookie(self, name, value):
        cookie_name = f'{name}'
        cookie_value = f'{value}'
        self.add_cookie(cookie_name, cookie_value)
        print(self.driver.get_cookie(cookie_name))

    def delete_specific_cookie(self, name):
        cookie_name = f'{name}'
        self.specific_cookie_deletion(cookie_name)

    def delete_all_cookies(self):
        self.all_cookies_deletion()


class LocalStorageManipulations(LocalStorage):
    def __init__(self, driver):
        super().__init__(driver)

    def all_elements_in_local_storage(self):
        for el in self.retrieve_local_storage():
            print(el)

    def specific_el_in_local_storage(self, element):
        storage_element = f'{element}'
        print(self.get_specific_storage_element(storage_element))

    def new_el_in_locale_storage(self, name, value):
        el_name = f'{name}'
        el_value = f'{value}'
        self.add_element_to_storage(el_name, el_value)
        print(self.driver.get_cookie(el_name))