# Check to see if a product page exists for a given item number
def productPageExists(context, itemNumber):
    itemURL = 'http://www.monoprice.com/Product?p_id=' + itemNumber
    context.browser.get(itemURL)
    return True

@given('item number {itemNumber} is available')
def step(context, itemNumber):
    # Make sure that the poduct page for the item exists
    assert productPageExists(context, itemNumber)

@when('a user searches for item number {itemNumber}')
def step(context, itemNumber):
    assert True

@then('the page for item number {itemNumber} should be displayed')
def step(context, itemNumber):
    assert True
