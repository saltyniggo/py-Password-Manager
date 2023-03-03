import random

masterPassword = '1234'
runToken = True
accessAttempts = 0

while runToken == True:
    print("Welcome to your password manager")
    print("")
    print(accessAttempts)
    print("Please enter the Master Password:")
    userMasterPassword = input("")
    if userMasterPassword == masterPassword:
        print("Access successful!")
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
