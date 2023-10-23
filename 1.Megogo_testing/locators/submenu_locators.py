class SubmenuLocatorsCollection:
    def __init__(self):
        self.__submenu_locator = ('xpath', '//a[@class="dropdown-toggle menu-link" '
                                           'and @href="javascript:void(0);"]//span')
        self.__max_subscription_locator = ('xpath', '//a[@data-subscription-id="2741"]')
        self.__ictv_locator = ('xpath', '/html/body/div[1]/div[4]/main/div[3]/div/div/div/div[2]/'
                                        'div/div/div/div[1]/div[2]/div/div/div[1]/div/div/a/img')
        self.__buy_top_box_button_locator = ('xpath', '//a[@class="pristavka__top--button"]')
        self.__gesture_lang_locator = ('xpath', '//img[@src='
                                                '"https://s4.vcdn.biz/static/f/5307981601/image.jpg/pt/r220x100x4"]')
        self.__movie1_for_deaf_locator = ('xpath', '//img[@src='
                                                   '"https://s1.vcdn.biz/static/f/2844833131/image.jpg/pt/r193x272x4"]')
        self.__search_input = ('xpath', '//input[@class and @type="text"]')

    @property
    def submenu_locator(self):
        return self.__submenu_locator

    @property
    def max_sub_locator(self):
        return self.__max_subscription_locator

    @property
    def ictv_locator(self):
        return self.__ictv_locator

    @property
    def buy_top_box_button_locator(self):
        return self.__buy_top_box_button_locator

    @property
    def gesture_lang_locator(self):
        return self.__gesture_lang_locator

    @property
    def movie1_for_deaf_locator(self):
        return self.__movie1_for_deaf_locator
