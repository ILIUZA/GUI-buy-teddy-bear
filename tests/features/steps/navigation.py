from behave import given, then


@given('User is on the Main Page')
def step_implementation(context):
    context.browser.get(context.main_page.url)
    context.browser.maximize_window()


@then('User is on the Cart Page')
def step_implementation(context):
    expected_url = context.cart_page.urlCartPage
    assert context.browser.current_url == expected_url
