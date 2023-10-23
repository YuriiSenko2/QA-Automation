from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def close_cookies_and_location(driver_name):
    web_driver_wait = WebDriverWait(driver_name, 10)
    cookies = '//a[@aria-label="dismiss cookie message"]'
    web_driver_wait.until(EC.presence_of_element_located(('xpath', cookies))).click()
    confirm_location = '//button[@class="recommendation-modal__button"]'
    web_driver_wait.until(EC.presence_of_element_located(('xpath', confirm_location))).click()
    return web_driver_wait
