from behave import given, when, then

@given(u'I navigate to the crime pages')
def nav(context):
    """
    Navigate to the crime pages
    """
    context.browser.get('http://localhost:2500/')

@when(u'I click on the link to date search')
def click(context):
    """
    Change to the date search pages
    """
    context.browser.find_element_by_partical_link_text('date_search').click()

@then(u'I should see the options of date')
def search(context):
    """
    if successful, then we should open the date search page
    """
    # use print(context.browse.date_search) to aid debugging
    print(context.browse.date_search)
    assert context.browser.current_url == 'http://localhost:2500/date_search'
