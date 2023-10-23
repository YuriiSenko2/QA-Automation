from Megogo_testing.pages.base_page import BasePage
from Megogo_testing.pages.submenu_categories_sub_pages import SubMenuPaths
from Megogo_testing.core.tuple_for_locators import LocatorTuple
from Megogo_testing.locators.submenu_locators import SubmenuLocatorsCollection


class SubmenuPages(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def if_channel_broadcasts_in_subscription(self):
        self._wait_until_el_appears_to_click(LocatorTuple(*SubmenuLocatorsCollection().max_sub_locator))
        self._wait_until_is_clickable(LocatorTuple(*SubmenuLocatorsCollection().ictv_locator))
        return SubMenuPaths(self.driver)

    def check_buy_button_in_a_set_top_box(self):
        self._wait_until_is_clickable(LocatorTuple(*SubmenuLocatorsCollection().buy_top_box_button_locator))
        return SubMenuPaths(self.driver)

    def turn_on_a_video_in_a_dyvysiakchutno(self):
        self._wait_until_is_clickable(LocatorTuple(*SubmenuLocatorsCollection().gesture_lang_locator))
        self._wait_until_is_clickable(LocatorTuple(*SubmenuLocatorsCollection().movie1_for_deaf_locator))
        return SubMenuPaths(self.driver)

