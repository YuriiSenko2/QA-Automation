from selenium.webdriver import Chrome


def launch_from_the_main_page():
    driver = Chrome('miami_heat_store_testing/drivers/chromedriver.exe')
    driver.get('https://www.themiamiheatstore.com/')
    return driver


def launch_from_the_jersey_page():
    driver = Chrome('miami_heat_store_testing/drivers/chromedriver.exe')
    driver.get('https://www.themiamiheatstore.com/collections/jerseys')
    return driver
