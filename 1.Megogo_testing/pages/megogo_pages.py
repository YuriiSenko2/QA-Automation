from selenium.webdriver.chrome.webdriver import WebDriver
from Megogo_testing.pages.base_page import BasePage
from Megogo_testing.pages.submenu_categories_pages import SubmenuPages
from Megogo_testing.core.tuple_for_locators import LocatorTuple
from Megogo_testing.locators.submenu_locators import SubmenuLocatorsCollection
from Megogo_testing.pages.widgets_pages import WidgetsPages
from Megogo_testing.locators.widgets_locators import WidgetsLocatorsCollection
from Megogo_testing.pages.header_nav_pages import HeaderNavPages
from Megogo_testing.pages.sign_in_pages import SignInPages
from Megogo_testing.locators.sign_in_locators import SignInLocatorsCollection


class SignIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_sign_in_button(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*SignInLocatorsCollection().sign_in_button))

    def sign_in_to_account(self):
        return SignInPages(self.driver)


class Submenu(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_on_submenu(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*SubmenuLocatorsCollection().submenu_locator))

    def choose_submenu_option(self, selection):
        self._wait_until_el_appears_to_click(LocatorTuple('xpath', f'//a[@class="submenu-link" '
                                                                   f'and @href="https://megogo.net/ua/{selection}"]'))
        return SubmenuPages(self.driver)


class Widgets(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.input = 'Світ навиворіт'

    def lang_button(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().language_button))

    def change_language(self, lang):
        self._wait_until_el_appears_to_click(LocatorTuple('xpath', f'//a[@class="link-default" '
                                                                   f'and @data-lang="{lang}"]//parent::span'))

    def i_watch_button(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().i_watch))

    def favourite_section(self, section):
        """There are 3 favourite sections in 'I watch' dropdown"""
        self._wait_until_el_appears_to_click(LocatorTuple('xpath', '//a[@class="link-default" and @href="https:'
                                                                   f'//megogo.net/ua/watching?sorting={section}"]'))

    def search_button(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().search_locator))

    def fill_search(self):
        self._wait_until_el_appears_for_input(LocatorTuple(*WidgetsLocatorsCollection().search_filler), self.input)

    def find_and_turn_on_a_video(self):
        return WidgetsPages(self.driver)

    def add_remove_from_favourites(self):
        return WidgetsPages(self.driver)

    def click_on_fares(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().fares_locator))

    def sub_campaign_pages(self):
        return WidgetsPages(self.driver)


class HeaderNav(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def choose_menu_option(self, option):
        locator = (LocatorTuple('xpath', f'//a[@class="dropdown-toggle menu-link" and @href="https://megogo.net/ua/{option}/main"]//span'))
        self._wait_until_el_appears_to_click(locator)

    def choose_filter_option(self, option):
        locator = (LocatorTuple('xpath', f'//div[@data-tracker-title="{option}"]'))
        self._wait_until_el_appears_to_click(locator)

    def choose_year(self, option):
        locator = (LocatorTuple('xpath', f'//a[@data-filter-value="{option}"]'))
        self._wait_until_el_appears_to_click(locator)

    def cartoon_pages(self):
        return HeaderNavPages(self.driver)

    def filter_page(self):
        return HeaderNavPages(self.driver)

    def football_highlights_page(self):
        return HeaderNavPages(self.driver)



