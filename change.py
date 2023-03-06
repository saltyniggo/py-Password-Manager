from sqlite3 import connect
from subprocess import call

conn = connect('donthackmeplease.db')


def changedata():
    updateaccount = input("For which account do you want to change the password?: ")
    call("clear", shell=True)
    updatepassword = input("Please enter the new password: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE account = ?",
                (updateaccount,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No matching account found.")
    else:
        conn.execute("UPDATE passwords SET password = ? WHERE account = ?", (updatepassword, updateaccount))
        conn.commit()
        print("Data updated")
