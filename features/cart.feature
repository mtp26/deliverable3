Feature: The ability to add and remove items from a shopping cart

Scenario: Add a single item to an empty cart
        Given the shopping cart is empty
        When we add an item to the cart
        Then the page should display that there is 1 items in the cart


Scenario: Remove an item from a cart, leaving the cart empty
        Given there is an item in the shopping cart
        When we remove 1 item from the cart
        Then the page should display that there is 0 items in the cart