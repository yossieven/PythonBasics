from Database import Database


def insert(title, author, year, isbn):
    with Database() as db:
        db.execute("INSERT INTO store VALUES(DEFAULT, %s, %s, %s, %s)", (title, author, year, isbn))


def view():
    with Database() as db:
        db.execute("SELECT * FROM store ORDER BY 1")
        rows = db.fetchall()
    return rows


def search(title="", author="", year="", isbn=""):
    title = '%'+title+'%'
    author = '%'+author+'%'
    year = '%'+year+'%'
    isbn = '%'+isbn+'%'
    with Database() as db:
        db.execute("SELECT * FROM store WHERE title like %s and author like %s and year like %s and isbn like %s",
                   (title, author, year, isbn))
        rows = db.fetchall()
    return rows


def delete(entry_id):
    try:
        with Database() as db:
            db.execute("DELETE FROM store WHERE id=%s", (entry_id,))
    except Exception as e:
        print("failed to delete: " + str(e))


def update(book_id, title, author, year, isbn):
    try:
        with Database() as db:
            db.execute("UPDATE store SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, book_id))
    except Exception as e:
        print("failed to update: " + str(e))

# insert('a book', 'John Smith', '1999', '543324324')
# print(view())
# print(search(author='John Smith'))
# print(view())
# delete(7)
# print(view())
# update(1, 'Another one', 'Yossi Even', '1998', '999888777')
# print(view())
