import re

@given(u'the wish list is empty')
def step(context):
    context.browser.delete_all_cookies()
    assert True

@when('we add an item to the wish list')
def step(context):
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=10532&p_quantity=1')

@then('the page should display that there is {count} row in the wish list')
def step(context, count):

    wishListCount = len(context.browser.find_elements_by_xpath("//table[@class='ma-table']/tbody/tr"))
    print(wishListCount)

    # Assert number of rows of wish list - 2 = number expected.
    assert (wishListCount-2 == int(count))


@given(u'the wish list is blank')
def step(context):
    context.browser.delete_all_cookies()
    context.browser.refresh()
    assert True

@when('we add two different items to the wish list')
def step(context):
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=10532&p_quantity=1')
    context.browser.refresh()
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=2747&p_quantity=1')

@then('the wish list should display {count} rows')
def step(context, count):

    wishList = context.browser.find_elements_by_xpath("//table[@class='ma-table']/tbody/tr")

    wishListCount = len(wishList)
    print(wishListCount)

    # Assert number of rows of wish list - 2 = number expected.
    assert (wishListCount-2 == int(count))


@given(u'the wish list has one item')
def step(context):
    context.browser.delete_all_cookies()
    context.browser.refresh()
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=10532&p_quantity=1')
    assert True

@when('we add the same item again')
def step(context):
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=10532&p_quantity=1')

@then('the quantity of the item should be {count}')
def step(context, count):

    quantity = context.browser.find_element_by_xpath("//table[@class='ma-table']/tbody/tr/td/input[@name='p_quantity']").get_attribute('value')
    print("quantity",quantity)
    print("count",count)

    assert (int(quantity) == int(count))


@given(u'the wish list has 1 item')
def step(context):
    context.browser.delete_all_cookies()
    context.browser.refresh()
    context.browser.get('http://www.monoprice.com/Product/ProductSavedListUpdate?p_id=10532&p_quantity=1')
    assert True

@when('we move the item to the shopping cart')
def step(context):
    context.browser.find_element_by_name('ca_move').click()
    context.browser.find_element_by_xpath("//span[@id='move_tab']/input").click()


@then('the shopping cart should have {count} item')
def step(context, count):

    itemCountText = context.browser.find_element_by_id('myBagCount').get_attribute('innerHTML')

    # Get the integer value of item count
    itemCount = [int(s) for s in itemCountText.split() if s.isdigit()][0]
    assert (itemCount == int(count))