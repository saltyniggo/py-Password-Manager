from sqlite3 import connect
from subprocess import call

conn = connect('donthackmeplease.db')


def accessdata():
    accountlogin = input("Which login data do you need?: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE account = ?",
                (accountlogin,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No matching login data found.")
    else:
        for row in rows:
            call("clear", shell=True)
            print(row)
