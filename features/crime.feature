Feature: crime
"""
Confirm that we can browse the crime data and search pages on our site.
"""

Scenario: success for visiting crime data pages
    Given I navigate to the crime pages
    When I click on the link to date search
    Then I should see the options of date