Feature: adding cart item

Scenario: add a single item to cart
        When we add one item to the cart
        Then the cart should display one item
