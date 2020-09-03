from behave import when, then


@when('User can see the results of search (not empty)')
def step_implementation(context):
    results = context.main_page.resultsList()
    assert results is not None


@then('User can see the added items in the cart')
def step_implementation(context):
    if context.response is not None:
        assert context.cart_page.itemIsInCart(context.response) is True
