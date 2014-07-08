# Check to see if a product page exists for a given item number
def productPageExists(context, itemNumber):
    itemURL = 'http://www.monoprice.com/Product?p_id=' + itemNumber
    request = context.browser.get(itemURL)
    print request.status_code
    return True

@given('item number {itemNumber} is available')
def step(context):
    # Make sure that the poduct page for the item exists
    assert productPageExists(itemNumber)
