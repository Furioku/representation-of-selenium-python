Feature: We would like to check login page:
1. Please verify if cookies banner appears and work correctly
2. Check if loging feature works

Scenario Outline: Scenario Outline name: User can login into the appliccation
    Given User start at login page
    Then User is able to see cookies information banner and verify text in title banner
    When User press Only Allow Essential Cookies button
    Then User is able to see email and password input fields
    When User type proper <email> into email input field
    And User type proper <password> into password input field
    And User click on Logg inn button
    Then User should land on application home page
    Examples:
        | email                         | password           |
        | philippsalata4@gmail.com      | MaRPhF39$97!22     |
        | philippsalata3@gmail.com      | Lkdygc$SE$         |