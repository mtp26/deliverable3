import re

# Link to the item that we're using for testing
itemURL = 'http://www.monoprice.com/Product?c_id=109&cp_id=10904&cs_id=1090407&p_id=10532&seq=1&format=2'

# Regular price for the item
regularPrice = 79.48

# Volume pricing for buying more than one item when adding two items to the cart
volumePrice = 78.50

# Link to the cart page
cartURL = 'http://www.monoprice.com/Cart'


# Helper function to get the item count from the shopping cart of monoprice.com
def getCartItemCount(context):
    context.browser.implicitly_wait(10)
    context.browser.get(cartURL)
    itemCountText = context.browser.find_element_by_id('myBagCount').get_attribute('innerHTML')
    # Get the integer value of item count
    itemCount = [int(s) for s in itemCountText.split() if s.isdigit()][0]
    return itemCount

# Return a float of the item's price given a string containing the price
def getPrice(priceStr):
    # Get rid of any possible commas and parse out the float value
    return float(re.findall(r'\d+\.\d+', priceStr.replace(',',''))[0])

# Get the price subtotal of the items in the cart
def getCartSubtotal(context):
    context.browser.implicitly_wait(10)
    context.browser.get(cartURL)
    cartPriceText = context.browser.find_element_by_id('myBagSubTotal').get_attribute('innerHTML')
    # Get the integer value of item count
    cartPrice = getPrice(cartPriceText)
    return cartPrice 

# Get the item price given the item's page
def getItemPrice(context, itemURL):
    context.browser.implicitly_wait(10)
    context.browser.get(itemURL)
    itemPriceText = context.browser.find_element_by_css_selector('.price').get_attribute('innerHTML')
    # Get only the price value
    itemPrice = getPrice(itemPriceText)
    return itemPrice

@given('the shopping cart is empty')
def step(context):
    # Clear all of the session cookies, which leaves an empty cart
    context.browser.delete_all_cookies()

    # Check just to make sure that it's actually empty
    assert (getCartItemCount(context) == 0)

@when('we add an item to the cart')
def step(context):
    context.browser.get(itemURL)
    context.browser.find_element_by_css_selector('.button-yellow-large').click()

@then('the cart page should display that there are {count} items in the cart')
def step(context, count):
    assert (getCartItemCount(context) == int(count))

@given('there is an item in the shopping cart')
def step(context):
    # Make sure the cart is empty
    context.execute_steps(u'given the shopping cart is empty')

    # Add an item to the cart using the previous step definition
    context.execute_steps(u'when we add an item to the cart')

    # Check just to make sure that there actually is an item in the cart
    assert (getCartItemCount(context) == 1)

@when('we remove an item from the cart')
def step(context):
    context.browser.implicitly_wait(10)
    context.browser.get(cartURL)
    context.browser.find_element_by_css_selector('.js-remove-item').click()

@then('should show the subtotal of the items')
def step(context):
    # Make sure that the test item price is what we're expecting
    assert (getItemPrice(context,itemURL) == regularPrice)

    # Make sure that the subtotal is twice the cost of the item in volume pricing
    assert (getCartSubtotal(context) == (volumePrice*2))
