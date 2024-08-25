import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(browser, delay_seconds=10, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        EC.presence_of_element_located((by, value))
    )


def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = wait_element(browser, by=By.CSS_SELECTOR, value="button.btn-add-to-basket")
    print(button.text)
    assert button.is_displayed()
    time.sleep(5)
