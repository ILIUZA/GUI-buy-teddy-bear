import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from tests.locators.item_page import CartPageLocators
from tests.locators.main_page import MainPageLocators
from tests.pageobjects.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    @property
    def url(self):
        return super(MainPage, self).url + '/'

    def searchPhrase(self, phrase):
        self.enterText(MainPageLocators.searchInput, phrase)
        self.clickElement(MainPageLocators.searchButton)
        self.waitVisibility(MainPageLocators.searchResultInfo)

    def sortResults(self, sort_name):
        try:
            self.clickElement(MainPageLocators.sortButton)

            self.waitVisibility(MainPageLocators.sortOptionsDiv)
            div = self.browser.find_element(*MainPageLocators.sortOptionsDiv)
            locator = '//a[contains(text(), "' + sort_name + '")]'
            option = div.find_element_by_xpath(locator)
            option.click()
        except NoSuchElementException:
            print("I can't sort the results")

    def clickCartButton(self):
        self.clickElement(MainPageLocators.cartButton)

    def setFilterAge(self, age):
        try:
            self.waitVisibility(MainPageLocators.filterAgeLabel)
            locator = "li[aria-label='" + age + "']> span>a>div"
            filter_name = self.browser.find_element_by_css_selector(locator)

            actions = ActionChains(self.browser)
            actions.click(on_element=filter_name)
            actions.move_to_element(filter_name).perform()
        except:
            print("I can't find a filter or a value to filter results by Age")

    def resultsList(self):
        self.waitVisibility(MainPageLocators.searchResultList)
        return self.browser.find_elements(*MainPageLocators.searchResultList)

    def addItemInCart(self, i):
        i = int(i)
        my_list = self.resultsList()
        if my_list is not None:
            try:
                item_link = my_list[i - 1].find_element_by_tag_name("a")
                # Save the current window
                main_window = self.browser.current_window_handle

                # Open the link in a new tab by sending keystrokes on the element
                item_link.send_keys(Keys.CONTROL + Keys.ENTER)
                self.browser.switch_to.window(self.browser.window_handles[1])
                # Add an item in the Cart
                self.waitVisibility(CartPageLocators.addToCartButton)
                self.browser.find_element(*CartPageLocators.addToCartButton).click()
                self.waitVisibility(CartPageLocators.confirmText)
                time.sleep(3)

                self.browser.close()  # closes new tab

                self.browser.switch_to.window(main_window)

                return my_list[i - 1].get_attribute("data-asin")
            except:
                print("I can't add an item {}-th in the Cart".format(i))
        else:
            raise ValueError("The result list is empty")
