class HeaderNavLocatorsCollection:
    def __init__(self):
        """The Pytest sees only the full xpath and can't find even the following path in a self.__disney_page :
    ('xpath', '//div[@class="card sliderItem direction-vertical orientation-landscape size-large"]//div//div//
    a[@href="/ru/collection/multfilm_disney_ua"]//
    img[@src="https://s1.vcdn.biz/static/f/1539482761/image.jpg/pt/r220x100x4"]')"""
        self.__disney_page = ('xpath', '/html/body/div[1]/div[4]/main/section[2]/div/div/div/div/div[4]/div/div/a/img')
        self.__filter_page_locator = ('xpath', '//img[@src="https://s1.vcdn.biz/static/f/5781052891/'
                                               'image.jpg/pt/r220x100x4"]')
        self.__apply_button = ('xpath', '//span[@class="jsAcceptText"]')
        self.__sport_page = ('xpath', '//a[@class="dropdown-toggle menu-link" '
                                      'and @href="https://megogo.net/ua/sport/main"]')
        """Sport is different from other nav options since it has own submenu but one doesn't have to use it 
        and may simply go to the section by clicking Sport tab"""
        self.__football_page = ('xpath', '//img[@src="https://s5.vcdn.biz/static/f/5618431921/'
                                         'Futbol_ua.jpg/pt/r300x0x4"]')
        self.__football_highlights_page = ('xpath', '//a[@href="/ua/menu/football/highlights"]')

    @property
    def filter(self):
        return self.__filter_page_locator

    @property
    def disney_page(self):
        return self.__disney_page

    @property
    def apply(self):
        return self.__apply_button

    @property
    def sport_page(self):
        return self.__sport_page

    @property
    def football_page(self):
        return self.__football_page

    @property
    def football_highlights_page(self):
        return self.__football_highlights_page


