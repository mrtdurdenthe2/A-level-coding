username = input("Please enter your name")
password = input("Please enter your password")


if not bool(username.strip()):
    print("Please enter a name")



if len(password) < 10:
    print("Please enter a password thats atleast 10 characters")
else:
    print("password accepted")







