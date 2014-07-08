Feature: As a customer of Monoprice.com
         I want to be able to search for products by keyword and product number
         So that I can find what I may want to purchase

Scenario: Searching for a specific product number should take the user directly to the item's page
        Given item number 10532 is available
        When a user searches for item number 10532
        Then the page for item number 10532 should be displayed 

Scenario: Searching for a non-existent product ID should show zero results
        Given item number 3498948590398 is not available
        When a user searches for item number 3498948590398
        Then zero search results should be displayed
