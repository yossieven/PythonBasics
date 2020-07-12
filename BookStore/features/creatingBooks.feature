# Created by YOSEFEV at 12/07/2020
Feature: Creating Books
  All scenarios for creating new books

  Scenario: Adding a new book when specific book in store
    Given A specific book is in store
      | TITLE   | AUTHOR     | YEAR | ISBN          |
      | My book | Yossi Even | 2020 | ISBN#12121212 |
    When Creating a single new book
      | TITLE   | AUTHOR     | YEAR | ISBN          |
      | Another | Yossi Even | 2001 | ISBN#11143443 |
    Then Book is stored in the database
      | TITLE   | AUTHOR     | YEAR | ISBN          |
      | Another | Yossi Even | 2001 | ISBN#11143443 |
