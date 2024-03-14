"""
bfile = open("receipt.txt","r")
bfile["first"] = bfile["val"].str.extract(r'^\s*(.*?)\s*,')
bfile["second"] = bfile["val"].str.extract(r',\s*(.*?)\s*,')
bfile["third"] = bfile["val"].str.extract(r',\s*(.*?)\s*,')
bfile["forth"] = bfile["val"].str.extract(r',\s*([^,]*)$')

prdCalculation = [bfile["first"]], [bfile["second"]], bfile["third"], bfile["forth"]
for cloumn in prdCalculation: 
    print(sum(bfile["third"]*bfile["forth"]))

"""
bfile = ('receipt.txt')
with open(bfile, 'r') as file:
    for line in file:
        if "Organic" in line:
            print(line)