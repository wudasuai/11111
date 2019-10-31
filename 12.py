import sqlite3

conn=sqlite3.connect('mobile.db')
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS mobile (item TEXT,quantity INT ,price INT)')
conn.commit()
def insert_item(item,quantity,price):
    cur.execute('INSERT INTO mobile VALUES(?,?,?)',(item,quantity,price))
    conn.commit()

def view_all():
    cur.execute('SELECT * FROM moblie')
    rows=cur.fetchall()
    return rows

def search_one(item):
    cur.execute('SELECT * FROM moblie WHERE item=?',(item))
    one=cur.fetchone()
    return one

def update_one():
    pass

def remove_one():
    pass


if __name__ == "__main__":
    insert_item('iphone',1000,5000)
