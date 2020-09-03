from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome('d:/Projects/Pets/chromedriver.exe')
    # driver.implicitly_wait(10)

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()