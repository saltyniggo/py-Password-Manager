from sqlite3 import connect
from random import randint
from subprocess import call

masterPassword = '1234'
runToken = True
accessAttempts = 0
accessSucceeded = False


def accessdata():
    print("Which login data do you need?")
    print("all is also possible")
    accountlogin = input("")
    if accountlogin == "all":
        cur = conn.cursor()
        cur.execute("SELECT * FROM passwords")
        rows = cur.fetchall()
        if len(rows) == 0:
            print("No matching login data found.")
        else:
            for row in rows:
                call("clear", shell=True)
                print(row)
    else:
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


def deletedata():
    deleteaccount = input("Enter account: ")
    call("clear", shell=True)
    deletepassword = input("Enter password: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE account = ? AND password = ?",
                (deleteaccount, deletepassword))
    rows = cur.fetchall()
    if len(rows) == 0:
        call("clear", shell=True)
        print("No matching account found.")
    else:
        conn.execute("DELETE FROM passwords WHERE account = ? AND password = ?", (deleteaccount, deletepassword))
        conn.commit()
        call("clear", shell=True)
        print("Data deleted")


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


while runToken:
    if not accessSucceeded:
        call("clear", shell=True)
        print("Welcome to your password manager")
        print("")
        print("Please enter the Master Password:")
        userMasterPassword: str = input()
        call("clear", shell=True)
    if userMasterPassword == masterPassword or accessSucceeded:
        if not accessSucceeded:
            accessSucceeded = True
            print("Access successful!")
        conn = connect('donthackmeplease.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (account TEXT,
                      website TEXT,
                      email TEXT,
                      username TEXT,
                      password TEXT NOT NULL);''')
        print("What do you want to do?:")
        print("1 - Access Data")
        print("2 - Input Data")
        print("3 - Change Data")
        print("4 - Delete Data")
        userSelection = input('')
        call("clear", shell=True)
        if userSelection == '1':
            accessdata()
        elif userSelection == '2':
            inputdata()
        elif userSelection == '3':
            changedata()
        elif userSelection == '4':
            deletedata()
        else:
            print("Wrong input")

    elif accessAttempts >= 5:
        verifyX = randint(1, 10)
        verifyY = randint(1, 10)
        verifySolution = verifyX + verifyY
        print("You have failed too many times.")
        print("Please verify that you are a human.")
        print(f"What is {verifyX} + {verifyY}?")
        verifyInput = input()
        call("clear", shell=True)
        verifyInput = int(verifyInput)
        if verifyInput == verifySolution:
            print("Alright, try again to access!")
            accessAttempts = 0
        else:
            print("Poorly that was not the right answer :(")
            runToken = False
    else:
        accessAttempts += 1
