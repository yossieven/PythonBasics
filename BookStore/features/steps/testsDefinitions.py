from behave import *

from BookStore.Database import Database


@given("An empty bookstore")
def step_empty_bookstore():
    with Database() as db:
        db.execute("DELETE FROM store")


@given("A single book in store")
def step_a_single_book_in_store():
    with Database() as db:
        if len(db.fetchall()) > 1:
            db.execute("DELETE FROM store")
            db.execute("INSERT INTO store VALUES('A Book', 'Yossi Even', '2020', 'ISBN11223344')")
        elif len(db.fetchall()) == 0:
            db.execute("INSERT INTO store VALUES('A Book', 'Yossi Even', '2020', 'ISBN11223344')")
        else:
            return


@given("A specific book is in store")
def step_a_specific_book_in_store(context):
    with Database() as db:
        db.execute("DELETE FROM store")
        book = context.table[0]
        print(book)
        db.execute("INSERT INTO store VALUES (%s, %s, %s, %s)", (book['TITLE'], book['AUTHOR'], book['YEAR'], book['ISBN']))


@when("Creating a single new book")
def step_creating_a_single_new_book(context):
    with Database() as db:
        book = context.table[0]
        db.execute("INSERT INTO store VALUES (%s, %s, %s, %s)", (book['TITLE'], book['AUTHOR'], book['YEAR'], book['ISBN']))


@then("Book is stored in the database")
def step_book_is_stored_in_db(context):
    with Database() as db:
        print(context.table[0]['ISBN'])
        db.execute("SELECT * FROM store WHERE isbn=%s", (context.table[0]['ISBN'],))
        assert len(db.fetchall()) == 1
