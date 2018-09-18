import sqlite3

def connect():
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS city (ID    INT,
                                                    NAME           TEXT    NOT NULL,
                                                    COUNTRYCODE            TEXT     NOT NULL,
                                                    DISTRICT        TEXT,
                                                    POPULATION         INT);''')
    conn.commit()
    conn.close()

def insert(ids,name,countrycode,district,population):
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO city VALUES (?,?,?,?,?)",(ids,name,countrycode,district,population))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM city")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(ids="",name="",countrycode="",district="",population=""):
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM city WHERE ID=? OR name=? OR countrycode=? OR district=? OR population=?", (ids,name,countrycode,district,population))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(ids):
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM city WHERE id=?",(ids,))
    conn.commit()
    conn.close()

def update(previd,ids,name,countrycode,district,population):
    conn=sqlite3.connect("world.db")
    cur=conn.cursor()
    cur.execute("UPDATE city SET id=?, name=?, countrycode=?, district=?, population=? WHERE id=?",(ids,name,countrycode,district,population,previd))
    conn.commit()
    conn.close()

connect()

#print(view())

