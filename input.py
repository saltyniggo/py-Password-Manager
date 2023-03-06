import sqlite3

conn = sqlite3.connect('donthackmeplease.db')


def inputdata():
    account = input("Enter account: ")
    website = input("Enter website: ")
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE account = ? AND website = ? AND email = ? AND username = ? AND password = ?",
                (account, website, email, username, password))
    existing_data = cur.fetchone()
    if existing_data:
        print("Login data already exists for this account.")
    else:
        conn.execute("INSERT INTO passwords (account, website, email, username, password) VALUES (?, ?, ?, ?, ?)",
                     (account, website, email, username, password))
        conn.commit()
        print("Login data added successfully.")
