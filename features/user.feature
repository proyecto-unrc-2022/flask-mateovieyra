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
      {"status": "true"}
      """
    Then I retrieve the customer 'mateo'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Mateo Vieyra |

  Scenario: Retrieve all users
    Given the users 'mateo' an 'lucio' are in the system
    When I retrieve all users 
    Then I should get a '200' response
    And the following users are returned 
      | name         |
      | Mateo Vieyra |
      | Lucio Mansilla |

  Scenario: Edit a user 
    Given I have the user 'mateo' with name 'Mateo Vieyra'
    When I edit the user 'mateo' and change his name to 'Vieyra Mateo'
    Then I should get a '201' response 
    Then I retrieve the customer 'mateo'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Vieyra Mateo |
  
  Scenario: Delete a user 
    Given I have the user 'mateo' with name 'Mateo Vieyra'
    When I delete the user 'mateo'
    Then I should get a '200' response 
    Then I retrieve the customer 'mateo'
    Then I should get a '404' response

  
