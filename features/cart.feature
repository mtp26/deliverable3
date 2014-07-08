Feature: The ability to add and remove items from a shopping cart 
         and have the cart display the correct quantities and prices

Scenario: Add a single item to an empty cart
        Given the shopping cart is empty
        When we add an item to the cart
        Then the cart page should display that there are 1 items in the cart


Scenario: Remove an item from a cart, leaving the cart empty
        Given there is an item in the shopping cart
        When we remove an item from the cart
        Then the cart page should display that there are 0 items in the cart

Scenario: Add an additional item to the cart.
          The quanity and the sum of prices should update appropriately.
        Given there is an item in the shopping cart
        When we add an item to the cart
        Then the cart page should display that there are 2 items in the cart
        And  should show the sum of the price of the items
