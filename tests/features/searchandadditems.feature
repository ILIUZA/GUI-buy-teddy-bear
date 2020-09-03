
Feature: Search and Add items in the Cart

  Scenario: Verification of adding items in the Cart
    Given User is on the Main Page
    When User searches for "teddybear"
    And User sorts the result according to "Customer Review"
    And User selects the filter Toys Age Range and sets values
    |value|
    |5 to 7 Years|
    And User can see the results of search (not empty)
    And User opens the following items in a new tab and add them in the Cart
      |number|
      |1|
      |2|
    And User clicks on the Cart Button
    Then User is on the Cart Page
    And User can see the added items in the cart
