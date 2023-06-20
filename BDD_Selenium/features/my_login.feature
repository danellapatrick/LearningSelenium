Feature: Login
  Scenario: Login into Facebook
    Given I launch Chrome browser
    When I open Facebook Page
    And Enter the username and Password
    And Click Login
    Then It should successfully login

