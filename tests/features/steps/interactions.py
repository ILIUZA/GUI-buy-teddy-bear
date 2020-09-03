from behave import when


@when('User searches for "{search_phrase}"')
def step_implementation(context, search_phrase):
    context.main_page.searchPhrase(search_phrase)


@when('User sorts the result according to "{sort_name}"')
def step_implementation(context, sort_name):
    context.main_page.sortResults(sort_name)


@when('User clicks on the Cart Button')
def step_implementation(context):
    context.main_page.clickCartButton()


@when('User selects the filter Toys Age Range and sets values')
def step_implementation(context):
    for row in context.table:
        context.main_page.setFilterAge(row['value'])


@when('User opens the following items in a new tab and add them in the Cart')
def step_implementation(context):
    for row in context.table:
        context.response = context.main_page.addItemInCart(row['number'])
        #print(context.response)
