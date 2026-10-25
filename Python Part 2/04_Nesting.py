uname= input("Enter user name:")
password= input("Enter password:")

if ("admin" == uname and "pass1" == password):
    print("Login seccesfully!")
elif ("admin" != uname and "pass1" != password):
    print("Wrong username and password!")
else:
    if ("admin" != uname):
        print("Wrong user name.")
    else:
        print("Wrong password")