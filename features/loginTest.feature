Feature: Login To The App

 Scenario: Login to sauce demo with valid credentials
  Given User launch chrome browser
   When Open Swag labs the web page
   And  Enter username "standard_user" and password "secret_sauce"
   And Click on login button
   Then Validate the product page


 Scenario Outline: Login to sauce demo with mutiple credentials
  Given User launch chrome browser
   When Open Swag labs the web page
   And  Enter username "<username>" and password "<password>"
   And Click on login button
   Then Validate the product page

   Examples:
    | username        | password     |
    | standard_user   | secret_sauce |
    | locked_out_user | secret_sauce | 
    | problem_user    | secret_sauce |