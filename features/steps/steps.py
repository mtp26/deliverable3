import re

# Helper function to get the item count from
# the shopping cart of monoprice.com
def getCartItemCount(context):
    itemCountText = context.browser.find_element_by_id('myBagCount').get_attribute('innerHTML')
    # Get the integer value of item count
    itemCount = [int(s) for s in itemCountText.split() if s.isdigit()][0]
    return itemCount

@given(u'the shopping cart is empty')
def step(context):
    # Clear all of the session cookies, which leaves an empty cart
    context.browser.delete_all_cookies()
    assert True

@when('we add an item to the cart')
def step(context):
    context.browser.get('http://www.monoprice.com/Product?c_id=109&cp_id=10904&cs_id=1090407&p_id=10532&seq=1&format=2')
    context.browser.find_element_by_css_selector('.button-yellow-large').click()

@then('the page should display that there is {count} items in the cart')
def step(context, count):
    assert (getCartItemCount(context) == int(count))
