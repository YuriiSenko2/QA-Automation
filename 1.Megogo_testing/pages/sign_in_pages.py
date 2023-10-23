from Megogo_testing.pages.base_page import BasePage
from Megogo_testing.pages.sign_in_path_page import SignInPaths
from Megogo_testing.core.tuple_for_locators import LocatorTuple
from Megogo_testing.locators.sign_in_locators import SignInLocatorsCollection


class SignInPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.number = '992344696'
        self.code = '5804'  # code is valid for 24 hours

    def get_confirmation_code(self):
        self._wait_until_el_appears_for_input(LocatorTuple(*SignInLocatorsCollection().phone_field), self.number)
        return SignInPaths

    def enter_confirmation_code(self):
        self._wait_until_el_appears_for_input(LocatorTuple(*SignInLocatorsCollection().code_field), self.code)
        return SignInPaths


