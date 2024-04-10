master_pwd = input("What is the master password? ")

def view(): #this is how to declare a function, this is a block of code who's proccesses will run when called upon. The name of the function follows "def" or define 
    pass

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add a new password or view existing ones (add/view), press q to quit? ")

    if mode == "q": 
        break

    if mode == "view": 
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue
