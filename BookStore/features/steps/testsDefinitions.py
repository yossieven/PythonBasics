from behave import *

from Database import Database


@given("An empty bookstore")
def step_empty_bookstore(context):
    with Database() as db:
        db.execute("DELETE FROM store")


@given("A single book in store")
def step_a_single_book_in_store(context):
    with Database() as db:
        db.execute("SELECT * FROM store")
        count = len(db.fetchall())
        if count > 1:
            db.execute("DELETE FROM store")
            db.execute("INSERT INTO store VALUES(DEFAULT, 'A Book', 'Yossi Even', '2020', 'ISBN11223344')")
        elif count == 0:
            db.execute("INSERT INTO store VALUES(DEFAULT, 'A Book', 'Yossi Even', '2020', 'ISBN11223344')")
        else:
            return


@given("A specific book is in store")
def step_a_specific_book_in_store(context):
    with Database() as db:
        db.execute("DELETE FROM store")
        book = context.table[0]
        print(book)
        db.execute("INSERT INTO store VALUES (DEFAULT, %s, %s, %s, %s)", (book['TITLE'], book['AUTHOR'], book['YEAR'], book['ISBN']))


@when("Creating a single new book")
def step_creating_a_single_new_book(context):
    with Database() as db:
        book = context.table[0]
        db.execute("INSERT INTO store VALUES (DEFAULT, %s, %s, %s, %s)", (book['TITLE'], book['AUTHOR'], book['YEAR'], book['ISBN']))


@then("Book is stored in the database")
def step_book_is_stored_in_db(context):
    with Database() as db:
        print(context.table[0]['ISBN'])
        db.execute("SELECT * FROM store WHERE isbn=%s", (context.table[0]['ISBN'],))
        assert len(db.fetchall()) == 1


@step('Store contains {number:d} books')
def step_contains_number_of_books(context, number):
    with Database() as db:
        db.execute("SELECT count(*) FROM store")
        result = db.fetchone()
        print(result[0])


@given("there are few books in the store")
def step_there_are_books_in_store(context):
    with Database() as db:
        db.execute("DELETE FROM store")
        for book in context.table:
            print(book)
            db.execute("INSERT INTO store VALUES (DEFAULT, %s, %s, %s, %s)", (book['TITLE'], book['AUTHOR'], book['YEAR'], book['ISBN']))

