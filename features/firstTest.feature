Feature: Open a web page

 Scenario: Logo presence
  Given launch chrome browser
   When open the web page
   Then verify the logo present in the page
   And close browser
  
 