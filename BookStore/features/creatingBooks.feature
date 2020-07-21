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

    Scenario: Adding first book to store
      Given An empty bookstore
      When Creating a single new book
        | TITLE   | AUTHOR     | YEAR | ISBN          |
        | Another | Yossi Even | 2001 | ISBN#11143443 |
      Then Book is stored in the database
        | TITLE   | AUTHOR     | YEAR | ISBN          |
        | Another | Yossi Even | 2001 | ISBN#11143443 |
      And Store contains 1 books

    Scenario: New book raises book count in store
      Given A single book in store
      When Creating a single new book
        | TITLE             | AUTHOR       | YEAR | ISBN           |
        | Lord of The Rings | J.R.R Tolkin | 1945 | ISBN0618260269 |
      Then Store contains 2 books

      Scenario: add book to full repository
        Given there are few books in the store
          | TITLE                 | AUTHOR                | YEAR | ISBN          |
          | Another               | Yossi Even            | 2001 | ISBN#11143443 |
          | The Assasin's curse   | Cassandra Rose Clarke | 2012 | 1908844019    |
          | The Lady of the Lake  | Andrzej Sapkowski     | 1999 | B01M4GH0GS    |
        When Creating a single new book
          | TITLE             | AUTHOR       | YEAR | ISBN           |
          | Lord of The Rings | J.R.R Tolkin | 1945 | ISBN0618260269 |
        Then Store contains 4 books
