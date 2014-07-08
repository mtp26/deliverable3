Feature: The ability to put items into shopping cart from wish list

Scenario: Move one item to shopping cart
        Given the wish list has 1 item
 		And the shopping cart is empty
        When we move the item to the shopping cart
        Then the shopping cart should have 1 item