@when('we visit google')  
def step(context):  
   context.browser.get('http://www.google.com')  
 
@then('it should have a title "Google"')  
def step(context):  
   assert context.browser.title == "Google" 

@when('we add one item to the cart')
def step(context):
    context.browser.get('http://www.monoprice.com/Product?c_id=109&cp_id=10904&cs_id=1090407&p_id=10532&seq=1&format=2')
    context.browser.find_element_by_css_selector('.button-yellow-large').click()

@then('the cart should display one item')
def step(context):
    itemCount = context.browser.find_element_by_id('myBagCount').get_attribute('innerHTML')
    print itemCount
    assert (itemCount == ' 1 items')
