from Megogo_testing.pages.base_page import BasePage
from Megogo_testing.pages.widgets_sub_pages import WidgetsPaths
from Megogo_testing.core.tuple_for_locators import LocatorTuple
from Megogo_testing.locators.widgets_locators import WidgetsLocatorsCollection
import time


class WidgetsPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def video_sub_in_search(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().card_page))
        time.sleep(3)
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().choose_particular_title))
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().choose_particular_video))
        return WidgetsPaths(self.driver)

    def add_rm_from_favourites(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().card_page))
        time.sleep(3)
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().add_or_rem_from_fav))
        return WidgetsPaths

    def light_sub_campaign(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().about_light_sub))
        return WidgetsPaths(self.driver)

    def opt_sub_campaign(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().about_opt_sub))
        return WidgetsPaths(self.driver)

    def max_sub_campaign(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*WidgetsLocatorsCollection().about_max_sub))
        return WidgetsPaths(self.driver)