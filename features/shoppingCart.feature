Feature: As a customer of Monoprice.com
         I want to be able to save items to a shopping cart
         So that I can keep track of what I’m about to purchase

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
        And  should show the subtotal of the items
