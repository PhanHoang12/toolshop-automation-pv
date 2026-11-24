Feature: Shopping cart calculation
  As a shopper
  I want the cart to calculate line prices and the total from the selected quantity
  So that I know how much I will pay before checking out

  Background:
    Given I am on the home page

  Scenario Outline: Adding a product updates the cart line price and total
    When I open the product "<product>"
    And I add it to the cart with quantity <quantity>
    And I open the shopping cart
    Then the cart contains "<product>" with quantity <quantity>
    And the cart line price and total equal the unit price times <quantity>

    Examples:
      | product            | quantity |
      | Combination Pliers | 1        |
      | Claw Hammer        | 3        |
