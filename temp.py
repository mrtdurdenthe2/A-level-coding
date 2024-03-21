import math
listitem = input("Input the item you want to search for")
mylist = ['fqpde', 'jywec', 'qkkbi', 'shmdi', 'shugi', 'unpqg', 'obldi', 'wafdz', 'bchlr', 'ylhsu']
lowerbound = 0
upperbound = len(mylist)-1

founditem = False

while founditem == False and lowerbound <= upperbound:
    midpoint = math.ceil(lowerbound + (upperbound - lowerbound)/2)
    if mylist[midpoint] == listitem:
        founditem = True
    elif mylist[midpoint] < listitem:
        lowerbound = midpoint + 1
    else:
        upperbound = midpoint - 1

if founditem == True:
    print(f"Item found at {midpoint}")

