Feature: The ability to add an item to an empty cart

Scenario: Add a single item to an empty cart
        Given the shopping cart is empty
        When we add an item to the cart
        Then the page should display that there is 1 item in the cart
