Feature: Google Search
  Scenario: Searching on Gooogle
     Given I am on Google search page
     When I search for "Behave Selenium"
     Then the search results page is displayed
