from tests.pageobjects.cart_page import CartPage
from tests.pageobjects.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context, scenario):
    # context.browser = webdriver.Chrome('d:/Projects/Pets/chromedriver.exe')

    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    options = Options()
    options.set_headless(headless=False)
    options.binary = binary
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True
    context.browser = webdriver.Firefox(firefox_options=options, capabilities=cap,
                                        executable_path=r'D:\Projects\Pets\geckodriver.exe')
    # Instances of Page Classes
    context.main_page = MainPage(context.browser)
    context.cart_page = CartPage(context.browser)

# def after_all(context):
#   context.browser.close()
