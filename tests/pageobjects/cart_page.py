from selenium.webdriver.common.by import By

from tests.pageobjects.base_page import BasePage


class CartPage(BasePage):
    @property
    def urlCartPage(self):
        return super(CartPage, self).url + '/gp/cart/view.html?ref_=nav_cart'

    def itemIsInCart(self, row):
        try:
            locator = 'div[data-name="Active Items"]'
            itemsInCartDiv = (By.CSS_SELECTOR, locator)
            self.waitVisibility(itemsInCartDiv)
            selector = locator + '> div[data-asin="' + row + '"]'
            if self.browser.find_element_by_css_selector(selector) is not None:
                return True
            else:
                return False
        except:
            print("I can't check if the item {}-th is in the Cart".format(row))
