Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Jason Bourne |

  Scenario: Store a new user 
    Given some users are in the system 
    When I store the user with key 'mateo' and value 'Mateo Vieyra'
    Then I should get a '201' response 
    And the following response is returned:
      """
      {"status":"true"}
      """
    When I retrieve the customer 'mateo'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Mateo Vieyra |