import re

@when('we visit google')  
def step(context):  
   context.browser.get('http://www.google.com')  
 
@then('it should have a title "Google"')  
def step(context):  
   assert context.browser.title == "Google" 

@given(u'the shopping cart is empty')
def step(context):
    assert True

@when('we add an item to the cart')
def step(context):
    context.browser.get('http://www.monoprice.com/Product?c_id=109&cp_id=10904&cs_id=1090407&p_id=10532&seq=1&format=2')
    context.browser.find_element_by_css_selector('.button-yellow-large').click()

@then('the page should display that there is {count} item in the cart')
def step(context, count):

    itemCountText = context.browser.find_element_by_id('myBagCount').get_attribute('innerHTML')

    # Get the integer value of item count
    itemCount = [int(s) for s in itemCountText.split() if s.isdigit()][0]
    assert (itemCount == int(count))
