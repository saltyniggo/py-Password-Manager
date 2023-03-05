import sqlite3

conn = sqlite3.connect('donthackmeplease.db')

def inputData():
    website = input("Enter website: ")
    email = input("Enter Email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    conn.execute("INSERT INTO passwords (website, email, username, password) VALUES (?, ?, ?, ?)",
                (website, email, username, password))
    conn.commit()