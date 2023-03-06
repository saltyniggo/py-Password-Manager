from sqlite3 import connect

conn = connect('donthackmeplease.db')
test

def changedata():
    updateaccount = input("For which account do you want to change the password?: ")
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
