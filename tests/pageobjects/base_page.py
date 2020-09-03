from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    __TIMEOUT = 10

    def __init__(self, browser):
        self.browser = browser

    @property
    def url(self):
        return 'https://www.amazon.com'

    def waitVisibility(self, locator):
        try:
            WebDriverWait(self.browser, self.__TIMEOUT).until(
                expected_conditions.visibility_of_all_elements_located(locator))
        except TimeoutException:
            print('TimeoutException: I am out of time. Elements are not visible.')

    def clickElement(self, locator):
        self.waitVisibility(locator)
        self.browser.find_element(*locator).click()

    def enterText(self, locator, text):
        self.waitVisibility(locator)
        self.browser.find_element(*locator).send_keys(text)
