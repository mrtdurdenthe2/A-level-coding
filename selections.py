parDuration = float(input("Input parking duration (hours)\n"))
blueBadge = input("Do you have a blue badge? Yes or no\n")

if parDuration <= 1:
    print("Your parking rate is £0 per hour")
elif parDuration > 1 and parDuration <=2:
    print("Your parking rate is £1 per hour")
elif parDuration > 2 and parDuration <=3:
    print("Your parking rate is £2.5 per hour")
elif parDuration > 3 and parDuration <=4:
    print("Your parking rate is £3.7 per hour")
elif parDuration > 4 and parDuration <=500:
    print("Your parking rate is £5 per hour")
else:
    ("Please enter a valid parking duration")






