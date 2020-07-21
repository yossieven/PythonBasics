import psycopg2

conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
curr = conn.cursor()


def create_table():
    curr.execute("create table IF NOT EXISTS store (item TEXT, quantity INTEGER, price FLOAT)")
    conn.commit()


def insert_data(item, quantity, price):
    curr.execute("insert into store values(%s,%s,%s)", (item, quantity, price))
    conn.commit()


def view_data():
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    return rows


def delete_item(item):
    curr.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()


def update_item(item, quantity, price):
    curr.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()


update_item('wine glass', 10, 3.5)
conn.close()
