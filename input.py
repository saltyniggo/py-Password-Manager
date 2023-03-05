import sqlite3

conn = sqlite3.connect('donthackmeplease.db')

def inputData():
    website = input("Enter website: ")
    email = input("Enter Email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE website = ? AND email = ? AND username = ? AND password = ?",
                (website, email, username, password))
    existing_data = cur.fetchone()
    if existing_data:
        print("Login data already exists for this account.")
    else:
        conn.execute("INSERT INTO passwords (website, email, username, password) VALUES (?, ?, ?, ?)",
                     (website, email, username, password))
        conn.commit()
        print("Login data added successfully.")

##test