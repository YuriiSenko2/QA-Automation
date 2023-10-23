import time


class TestSubmenu:
    def test_moving_to_channel_in_subscription(self, submenu, cookies):
        submenu.click_on_submenu()
        pick_subcategory = submenu.choose_submenu_option('kino_i_tv')
        pick_subcategory.if_channel_broadcasts_in_subscription()
        cookies.all_cookies()

    def test_moving_to_buy_button_in_set_top_box(self, submenu, cookies):
        submenu.click_on_submenu()
        pick_subcategory = submenu.choose_submenu_option('pristavka')
        pick_subcategory.check_buy_button_in_a_set_top_box()
        cookies.specific_cookie('__gfp_64b')

    def test_moving_to_video_for_deaf_in_dyvysakchutno(self, submenu, cookies):
        submenu.click_on_submenu()
        pick_subcategory = submenu.choose_submenu_option('dyvysyakchutno')
        pick_subcategory.turn_on_a_video_in_a_dyvysiakchutno()
        cookies.new_cookie('new_cookie', 'new_value')
        cookies.specific_cookie('new_cookie')


class TestWidgets:
    def test_search_to_video_page_and_turn_it_on(self, widgets, sign_in):
        sign_in.click_on_sign_in_button()
        signing_in = sign_in.sign_in_to_account()
        signing_in.get_confirmation_code()
        time.sleep(2)
        signing_in.enter_confirmation_code()
        time.sleep(2)
        widgets.search_button()
        widgets.fill_search()
        pick = widgets.find_and_turn_on_a_video()
        pick.video_sub_in_search()

    def test_adding_to_favourites(self, widgets, sign_in):
        sign_in.click_on_sign_in_button()
        signing_in = sign_in.sign_in_to_account()
        signing_in.get_confirmation_code()
        time.sleep(2)
        signing_in.enter_confirmation_code()
        time.sleep(2)
        widgets.search_button()
        widgets.fill_search()
        pick_add = widgets.add_remove_from_favourites()
        pick_add.add_rm_from_favourites()

    def test_removing_from_favourites(self, widgets, sign_in):
        sign_in.click_on_sign_in_button()
        signing_in = sign_in.sign_in_to_account()
        signing_in.get_confirmation_code()
        time.sleep(2)
        signing_in.enter_confirmation_code()
        time.sleep(2)
        widgets.i_watch_button()
        widgets.favourite_section('favourites')
        pick_remove = widgets.add_remove_from_favourites()
        pick_remove.add_rm_from_favourites()

    def test_light_sub_campaign_page(self, widgets, cookies):
        widgets.click_on_fares()
        pick = widgets.sub_campaign_pages()
        pick.light_sub_campaign()
        cookies.new_cookie('another_cookie', 'another_value')
        cookies.delete_specific_cookie('another_cookie')
        cookies.specific_cookie('another_cookie')

    def test_opt_sub_campaign_page(self, widgets):
        widgets.click_on_fares()
        pick = widgets.sub_campaign_pages()
        pick.opt_sub_campaign()

    def test_max_sub_campaign_page(self, widgets):
        widgets.click_on_fares()
        pick = widgets.sub_campaign_pages()
        pick.max_sub_campaign()

    def test_change_lang_to_english(self, widgets):
        widgets.lang_button()
        widgets.change_language('en')


class TestHeaderNav:
    def test_disney_picking(self, header_nav, local_storage, sign_in):
        header_nav.choose_menu_option('mult')
        pick = header_nav.cartoon_pages()
        pick.choose_disney_page()
        local_storage.all_elements_in_local_storage()

    def test_year_filter(self, header_nav):
        header_nav.choose_menu_option('show')
        pick = header_nav.filter_page()
        pick.choose_filter()
        header_nav.choose_filter_option('Год')
        header_nav.choose_year('2016-2019')
        pick.apply_filter()

    def test_moving_to_football_highlights(self, header_nav, local_storage):
        pick = header_nav.football_highlights_page()
        pick.football_highlights_page_in_sport_section()
        local_storage.new_el_in_locale_storage('new_element', 'new_el_value')
        local_storage.specific_el_in_local_storage('new_element')



