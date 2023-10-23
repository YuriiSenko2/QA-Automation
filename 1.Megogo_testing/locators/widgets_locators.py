class WidgetsLocatorsCollection:
    def __init__(self):
        self.__search_locator = ('xpath', '//button[@class="form-submit" and @type="submit"]')
        self.__language_button_locator = ('xpath', '//a[@class="dropdown-toggle languages-toggle"]//parent::span')
        self.__fill_search = ('xpath', '//input[@class and @type="text"]')
        self.__choose_card_page = ('xpath', '//img[@alt="Світ навиворіт" and @data-ll-status="loaded"]')
        self.__choose_specific_title_page = ('xpath', '//a[@data-page-title="Україна"]')
        self.__add_rem_from_favorites = ('xpath', '/html/body/div[2]/div[4]/main/section[1]/div[4]/div[1]/div/section/div/div[2]/div[2]/div/div[2]/div[2]/button')
        self.__i_watch_locator = ('xpath', '//a[@class="dropdown-toggle watching-toggle "]')
        self.__choose_particular_video = ('xpath', '/html/body/div[2]/div[4]/main/section[1]/div[5]/div[2]/div[3]/'
                                                   'div/div/div[2]/div/div/div/div[3]/div[1]/div[1]/a/img')
        self.__fares_locator = ('xpath', '//a[@href="https://megogo.net/ua/kino_i_tv" '
                                         'and @class="btn bordered try-and-buy-btn jsTryAndBuyBtn"]')
        self.__about_light_sub_campaign_locator = ('xpath', '//a[@href="https://megogo.net/light_ua"]')
        self.__about_opt_sub_campaign_locator = ('xpath', '//a[@href="https://megogo.net/optimal_ua"]')
        self.__about_max_sub_campaign_locator = ('xpath', '//a[@href="https://megogo.net/maximum_tb_ua"]')

    @property
    def i_watch(self):
        return self.__i_watch_locator

    @property
    def language_button(self):
        return self.__language_button_locator

    @property
    def search_locator(self):
        return self.__search_locator

    @property
    def search_filler(self):
        return self.__fill_search

    @property
    def card_page(self):
        return self.__choose_card_page

    @property
    def add_or_rem_from_fav(self):
        return self.__add_rem_from_favorites

    @property
    def choose_particular_title(self):
        return self.__choose_specific_title_page

    @property
    def choose_particular_video(self):
        return self.__choose_particular_video

    @property
    def fares_locator(self):
        return self.__fares_locator

    @property
    def about_light_sub(self):
        return self.__about_light_sub_campaign_locator

    @property
    def about_opt_sub(self):
        return self.__about_opt_sub_campaign_locator

    @property
    def about_max_sub(self):
        return self.__about_max_sub_campaign_locator
