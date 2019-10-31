import sqlite3

def creat_mobile():
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS car (item TEXT,quantity INT ,price INT)')
    conn.commit()
    conn.close()


def insert_item(item,quantity,price):
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO car VALUES(?,?,?)',(item,quantity,price))
    conn.commit()
    conn.close()

def view_all():
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM car')
    rows=cur.fetchall()
    conn.close()
    return rows

def search_one(item):
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM car WHERE item LIKE  ?',(item+'%',))
    rows=cur.fetchall()
    conn.close()
    return rows

def update_one(item,quantity,price):
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur=execute('UPDATE car SET quantity=?,price=? WHERE  item=?',(quantity,price,item))
    conn.commit()
    conn.close()

    
def remove_one(item):
    conn=sqlite3.connect('mobile.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM car WHERE item=?',(item))
    cur.commit()
    cur.close()


if __name__ == "__main__":
    insert_item('iphone',1000,5000)
