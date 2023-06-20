Feature: Check the srdb for
  Scenario: Logo presence on Padzee home Page
    Given launch chrome broswer
    When open orange hrm homepage
    Then verify that the logo present on the page
    And close browser