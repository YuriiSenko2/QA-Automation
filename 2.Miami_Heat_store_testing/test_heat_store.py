import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from miami_heat_store_testing.cookies_and_location import close_cookies_and_location
from miami_heat_store_testing.web_drivers_launch import launch_from_the_main_page
from miami_heat_store_testing.web_drivers_launch import launch_from_the_jersey_page


def test_signin():
    driver = launch_from_the_main_page()
    web_driver_wait = WebDriverWait(driver, 10)
    close_cookies_and_location(driver)

    sign_in = '//a[@class="accounts_nav.a" and text()="Account"]'
    web_driver_wait.until(EC.presence_of_element_located(('xpath', sign_in))).click()
    email_locator = '//input[@type="email" and @name="customer[email]"]'
    input_email = web_driver_wait.until(EC.presence_of_element_located(('xpath', email_locator)))
    input_email.send_keys('yuriisenko2@gmail.com')
    time.sleep(1)
    password_locator = '//input[@type="password" and @id="CustomerPassword"]'
    input_password = web_driver_wait.until(EC.presence_of_element_located(('xpath', password_locator)))
    input_password.send_keys('Mypassword12345', Keys.ENTER)
    time.sleep(3)

    usernames = ['Yurii', 'Yuriy']
    assert f'Hi, {usernames[0]}' in driver.page_source and f'Hi, {usernames[1]}' not in driver.page_source


def test_specific_player_all_products_search():
    driver = launch_from_the_main_page()
    web_driver_wait = WebDriverWait(driver, 10)
    close_cookies_and_location(driver)

    time.sleep(1)
    player_to_search = 'Jimmy Butler'
    search_locator = '//input[@class="js-yext-query yxt-SearchBar-input"]'
    search = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_locator)))
    search.send_keys(player_to_search, Keys.ENTER)

    f_name = 'Jimmy'
    s_name = 'Butler'
    assert f'https://www.themiamiheatstore.com/search?query={f_name}+{s_name}&referrerPageUrl=' \
           'https://www.themiamiheatstore.com/' in driver.current_url


def test_specific_price():
    driver = launch_from_the_jersey_page()
    web_driver_wait = WebDriverWait(driver, 10)
    close_cookies_and_location(driver)

    price = '/html/body/div[7]/main/wlm/section/div[2]/div/div[2]/aside/div/div/div[7]/div/ul/li[3]/div/a/i'
    web_driver_wait.until(EC.presence_of_element_located(('xpath', price)))
    driver.find_element(by='xpath', value=price).click()

    from_ = 50
    to = 100
    assert f"https://www.themiamiheatstore.com/collections/jerseys/{from_}-{to}" in driver.current_url


def test_moving_to_specific_page():
    driver = launch_from_the_jersey_page()
    web_driver_wait = WebDriverWait(driver, 10)
    close_cookies_and_location(driver)

    page = '//a[@href="/collections/jerseys?page=2"]'
    web_driver_wait.until(EC.presence_of_element_located(('xpath', page)))
    driver.find_element(by='xpath', value=page).click()

    page_n = 2
    assert f"https://www.themiamiheatstore.com/collections/jerseys?page={page_n}" in driver.current_url


def test_add_to_cart():
    driver = launch_from_the_jersey_page()
    web_driver_wait = WebDriverWait(driver, 10)
    close_cookies_and_location(driver)

    jersey = "//a[@id='Jimmy Butler Nike Miami Mashup Vol. 2 Swingman Jersey - Finals Edition' and " \
             "text()='Jimmy Butler Nike Miami Mashup Vol. 2 Swingman Jersey - Finals Edition']"
    web_driver_wait.until(EC.presence_of_element_located(('xpath', jersey)))
    driver.find_element(by='xpath', value=jersey).click()
    size_chart = "//div[@class='variant-grid']//parent::select"
    web_driver_wait.until(EC.presence_of_element_located(('xpath', size_chart)))
    driver.find_element(by='xpath', value=size_chart).click()
    specific_size = "//option[@data-sku='127931']"
    web_driver_wait.until(EC.presence_of_element_located(('xpath', specific_size)))
    driver.find_element(by='xpath', value=specific_size).click()
    quantity = "//button[@class='adjust adjust-plus']"
    web_driver_wait.until(EC.presence_of_element_located(('xpath', quantity)))
    driver.find_element(by='xpath', value=quantity).click()
    add_to_cart = "//button[@type='submit' and @name='add']"
    web_driver_wait.until(EC.presence_of_element_located(('xpath', add_to_cart)))
    driver.find_element(by='xpath', value=add_to_cart).click()
    check_cart = "//a[@href='/cart' and text()='Check Out']"
    web_driver_wait.until(EC.element_to_be_clickable(('xpath', check_cart)))
    driver.find_element(by='xpath', value=check_cart).click()

    assert '2 ITEMS' in driver.page_source and \
           'Jimmy Butler Nike Miami Mashup Vol. 2 Swingman Jersey - Finals Edition' in driver.page_source

