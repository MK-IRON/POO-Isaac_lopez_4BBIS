import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')   
    
def mainMenu():
    clear()
    print(" ...::: WELCOME TO INSTAGRAM :::...",
    "\nWhat are we going to do?",
    "\n(1).-Manage users")

    try:
        while True:
            if int(input("Please type an option: ")) == 1:
                return 1
            else:
                print("Please type a selected option")
    except:
        print("Please type a selected option")


def manageUsers():
     clear()
     print("...::: USER MANAGER :::...",)
     print("(1).-Create new user",
     "\n(2).-Get users",
     "\n(3).-Delete user")
     
     try:
        while True:
            opt = int(input("Please type an option: "))
            if opt == 1:
                return 1
            if opt == 2:
                return 2
     except:
         print("Please type a selected option")


def getUsers(users):
    clear()
    print("...::: GET USERS :::...")
    for i in range(len(users)):
        print(users[i].username)
    input("Press any key to continue...")

    
def createUser(user):
    clear()
    print("...::: CREATE NEW USER :::...")
    username = input("Username: ")
    password = input("Password: ")
    newUser = user(username,password)
    return newUser