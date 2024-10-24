Feature: Test Amazon App
    @appium
    Scenario: Skip sign on and check laptop
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt
    And I navigate to the laptop section
    Then I add the specified laptop to the cart

    @appium1
    Scenario Outline: Skip sign on and search for a product
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt
    Then I search for "<product_name>" in search bar

    Examples:
    |product_name|
    |hot wheels|

    @readjson
    Scenario: Load data from JSON
    Given I have JSON data
    Then I am able access JSON data

    @readexcel
    Scenario: Load data from Excel
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt
    When I read data from excel and search product

    @readdb
    Scenario: Load data from DB
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt   
    When I read data from db and search product

    # Test case 01_Pharmacy
    @01_Pharmacy
    Scenario: Search for specific medication
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt
    And I click on the "Pharmacy" button from navigation bar
    And I scroll down and click on the "Explore all the ways to save" button
    And I type "lipitor" in the search field
#    Then I receive relevant results

    # Test case 01_Automotive
    @01_Automotive
    Scenario: Add a car to garage
    Given the Amazon app is launched
    When I skip sign-in
    And I dismiss the address change prompt
    And I click on the browser menu button
    And I click on the "Automotive" button
    And I click on the "Automotive Parts & Accessories" button
    And I click on the "Add a new vehicle" button
#    And I select a vehicle type

