import random
import sqlite3
from access import accessData
from input import inputData

masterPassword = '1234'
runToken = True
accessAttempts = 0
accessSucceeded = False

while runToken == True:
    if accessSucceeded == False:
        print("Welcome to your password manager")
        print("")
        print("Please enter the Master Password:")
        userMasterPassword = input("")
    if userMasterPassword == masterPassword or accessSucceeded:
        if accessSucceeded == False:
            accessSucceeded = True
            print("Access successful!")
        conn = sqlite3.connect('donthackmeplease.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS passwords
                     (website TEXT,
                      email TEXT,
                      username TEXT,
                      password TEXT NOT NULL);''')
        print("Was willst du tun?:")
        userSelection = input('')
        if userSelection == '1':
            accessData()
        elif userSelection == '2':
            inputData()
        elif userSelection == '3':
            changeData()
        else:
            print("Wrong input")
    elif accessAttempts >= 5:
        verifyX = random.randint(1, 10)
        verifyY = random.randint(1, 10)
        verifySolution = verifyX + verifyY
        print("You have failed too many times.")
        print("Please verify that you are a human.")
        print(f"What is {verifyX} + {verifyY}?")
        verifyInput = input()
        verifyInput = int(verifyInput)
        if verifyInput == verifySolution:
            print("Alright, try again to access!")
            accessAttempts = 0
        else:
            print("Poorly that was not the right answer :(")
            runToken = False
    else:
        accessAttempts += 1
