import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMERY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

connect()

def insert():
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("INSERT INTO book VALUES (?,?,?,?)", (title, author, year, isbn)
    conn.commit()
    conn.close()
                   
    
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows
                
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("SELECT * FROM bool WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows
                
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()
                
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cur()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (itle, author, year, isbn, id))
    conn.commit()
    conn.close()
