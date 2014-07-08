Feature: As a customer of Monoprice.com
		I want to be able to save items to a wish list
		So that I can save purchases for a later time

Scenario: Add a single item to an empty wish list
        Given the wish list is empty
        When we add an item to the wish list
        Then the page should display that there is 1 row in the wish list

Scenario: Add another of the same item to the wish list
		Given the wish list has one item
		When we add the same item again
		Then the quantity of the item should be 2

Scenario: Add two different items to a wish list
        Given the wish list is blank
        When we add two different items to the wish list
        Then the wish list should display 2 rows

Scenario: Move one item to shopping cart
        Given the wish list has 1 item
        When we transfer the item to the cart
        Then the shopping cart should have 1 item