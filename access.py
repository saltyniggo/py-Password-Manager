import sqlite3

conn = sqlite3.connect('donthackmeplease.db')

def accessData():
    cursor = conn.execute("SELECT * FROM passwords")
    for row in cursor:
        print(row)
