from sqlite3 import connect
from random import randint
from access import accessdata
from input import inputdata
from change import changedata
from subprocess import call

masterPassword = '1234'
runToken = True
accessAttempts = 0
accessSucceeded = False

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
        userSelection = input('')
        call("clear", shell=True)
        if userSelection == '1':
            accessdata()
        elif userSelection == '2':
            inputdata()
        elif userSelection == '3':
            changedata()
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
