from selenium.webdriver.common.by import By


class MainPageLocators:
    # NAVIGATION_LINK = (By.ID, 'blog-link')
    searchInput = (By.ID, 'twotabsearchtextbox')
    searchButton = (By.CSS_SELECTOR, 'input.nav-input[value="Go"]')
    searchResultInfo = (By.CSS_SELECTOR, 'div.a-section.a-spacing-small.a-spacing-top-small')

    sortButton = (By.CSS_SELECTOR, 'form.aok-inline-block.a-spacing-none')
    sortOptionsDiv = (By.CSS_SELECTOR, '#a-popover-4 > div > div')

    filterAgeLabel = (By.ID, 'p_n_age_range-title')

    searchResultList = (By.CSS_SELECTOR, 'div:not(.AdHolder)[data-component-type=s-search-result]')

    cartButton = (By.ID, 'nav-cart')


    # //span[contains(text(),'results for')]

    # #a-popover-4 > div
    # sortOption = (By.XPATH, '//a[contains(text(), "Customer Review")]')




