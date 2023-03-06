from sqlite3 import connect
from subprocess import call

conn = connect('donthackmeplease.db')


def inputdata():
    account = input("Enter account: ")
    call("clear", shell=True)
    website = input("Enter website: ")
    call("clear", shell=True)
    email = input("Enter email: ")
    call("clear", shell=True)
    username = input("Enter username: ")
    call("clear", shell=True)
    password = input("Enter password: ")
    call("clear", shell=True)
    if account and password and (email or username):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM passwords WHERE account = ? AND website = ? AND email = ? AND username = ? AND password = ?",
            (account, website, email, username, password))
        existing_data = cur.fetchone()
        if existing_data:
            print("Login data already exists for this account.")
        else:
            conn.execute("INSERT INTO passwords (account, website, email, username, password) VALUES (?, ?, ?, ?, ?)",
                         (account, website, email, username, password))
            conn.commit()
            print("Login data added successfully.")
    else:
        print("Data missing, please try again")
