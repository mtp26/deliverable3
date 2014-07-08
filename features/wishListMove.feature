@shop
Feature: The ability to put items into shopping cart from wish list

Scenario: Move one item to shopping cart
        Given the wish list has 1 item
        When we transfer the item to the cart
        Then the shopping cart should have 1 item