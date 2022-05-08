import sqlite3

def connect(dbname):
    con = sqlite3.connect(dbname)
    con.execute("CREATE TABLE IF NOT EXISTS TRIP_HOTEL (NAME TEXT,PRICE INT)")
    print("TABLE CREATED SUCCESSFULLY")
    con.close()

def insert_into_table(dbname, values):
    con = sqlite3.connect(dbname)
    con.execute("INSERT INTO TRIP_HOTEL (NAME, PRICE) VALUES (?, ?)",values)
    con.close()

def get_hotel(dbname):
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    cur.execute("SELECT * FROM TRIP_HOTEL")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)
    con.close()