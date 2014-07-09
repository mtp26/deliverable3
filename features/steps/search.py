from selenium.webdriver.common.keys import Keys

# Get the item number from a current item page
def getItemNumber(context, itemURL):
    try:
        context.browser.get(itemURL)
        elem = context.browser.find_element_by_xpath("//div[@class='product-number']/span")
        return [int(s) for s in elem.get_attribute('innerHTML').split() if s.isdigit()][0]
    except:
        return -1

# Check to see if a product page exists for a given item number
def productPageExists(context, itemNumber):
    itemURL = 'http://www.monoprice.com/Product?p_id=' + itemNumber

    # The site redirects back to the home page instead of showing a 404
    # if the product page doesn't exist, so we actually need to check
    # the content of the page
    if getItemNumber(context, itemURL) == int(itemNumber):
        return True
    else:
        return False

@given('item number {itemNumber} is available')
def step(context, itemNumber):
    # Make sure that the poduct page for the item exists
    assert productPageExists(context, itemNumber)

@when('a user searches for item number {itemNumber}')
def step(context, itemNumber):
    # Search for the item number by simulating key presses
    searchURL = 'http:/www.monoprice.com/Search'
    context.browser.get(searchURL)
    elem = context.browser.find_element_by_css_selector('.search-input')
    elem.send_keys(itemNumber + Keys.RETURN)

@then('the page for item number {itemNumber} should be displayed')
def step(context, itemNumber):
    # Make sure we were redirected to the item's page
    currentURL = context.browser.current_url
    if getItemNumber(context, currentURL) == int(itemNumber):
        return True
    else:
        return False

@given('item number {itemNumber} is not available')
def step(context, itemNumber):
    # Make sure that a poduct page for a supposedly 
    # non-existent item does not exit
    assert not productPageExists(context, itemNumber)

@then('zero search results should be displayed')
def step(context):
    # Find the search result text and make sure it's zero
    elems = context.browser.find_elements_by_xpath("//td[contains(@style,'font-weight:bold')]/font")
    assert (elems[1].get_attribute('innerHTML') == '0')
