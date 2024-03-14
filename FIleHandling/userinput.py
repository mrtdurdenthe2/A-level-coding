file_path = 'studentlist.txt'
try:
    with open(file_path, 'x') as file:
        print("Test")
except FileExistsError:
    print("The file already exists.")
 
studentInfo = []
StudentID = studentInfo.append(input("Enter your student id\n"))
StudentName = studentInfo.append(input("Enter your student name\n"))
Major = studentInfo.append(input("Enter your major\n"))
DateOfBirth = studentInfo.append(input("Enter your date of birth\n"))


finished = input("Enter 'done' when finished\n")
if "done" or "Done" in finished:
        print("Finished")
else:
    print("\n")

with open(file_path, mode="w") as file:
    file.write(", ".join(studentInfo, "\n"))

with open (file_path, 'rt') as myfile:    
    for myline in myfile:                   
        if "science" or "Science" in myline:
             print(myline)
            