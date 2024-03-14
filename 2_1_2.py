'''
Length = float(input("Whats the length?\n"))
Height = float(input("Whats the height?\n"))
Width = float(input("Whats the width?\n"))
print("Volume =", Length*Height*Width, "\n")
'''

StudNum = int(input("How many students are there?"))
studentscores = []

for i in range(StudNum):
    studentscore = int(input(f"Enter the test score the for student {i + 1} (0-100): "))
    while studentscore < 0 or studentscore > 100:
        studentscore = int(input("Enter a score between 0 and 100: /n"))
        
    studentscores.append(studentscore)
    
highest_score = max(studentscores)
lowest_score = min(studentscores)
average_score = sum(studentscores) / StudNum

print("Your highest score is", highest_score, "/n", "Your lowest score is", lowest_score, "/n", "Your average score is", average_score, "/n")
    
