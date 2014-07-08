Feature: The ability to add more than one item to the wish list

Scenario: Add two different items to a wish list
        Given the wish list is blank
        When we add two different items to the wish list
        Then the wish list should display 2 rows