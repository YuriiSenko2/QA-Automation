from Megogo_testing.pages.base_page import BasePage
from Megogo_testing.pages.header_nav_sub_pages import HeaderNavPaths
from Megogo_testing.core.tuple_for_locators import LocatorTuple
from Megogo_testing.locators.header_nav_locators import HeaderNavLocatorsCollection


class HeaderNavPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_disney_page(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().disney_page))
        return HeaderNavPaths(self.driver)

    def choose_filter(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().filter))
        return HeaderNavPaths(self.driver)

    def apply_filter(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().apply))
        return HeaderNavPaths(self.driver)

    def football_highlights_page_in_sport_section(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().sport_page))
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().football_page))
        self._wait_until_el_appears_to_click(LocatorTuple(*HeaderNavLocatorsCollection().football_highlights_page))
        return HeaderNavPaths(self.driver)