
def existingUsers():
    firstname = input("Input firstname\n")[0:3]
    lastname = input("Input Lastname\n")[0:3]
    currentnumber = 0
    numbername = firstname+lastname+f"{currentnumber+1}"
    print("Name concatted (",numbername,")")
    database = []    
    while numbername in database and currentnumber<999:
        numbername = firstname+lastname+f"{currentnumber+1}"
    else:
        print("Username Accepted")

existingUsers()




