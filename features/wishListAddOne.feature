Feature: The ability to add a single item to a wish list

Scenario: Add a single item to an empty wish list
        Given the wish list is empty
        When we add an item to the wish list
        Then the page should display that there is 1 row in the wish list

Scenario: Add another of the same item to the wish list
		Given the wish list has one item
		When we add the same item again
		Then the quantity of the item should be 2

