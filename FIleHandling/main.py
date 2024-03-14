bookFile = open("BookList.txt","r")
test = bookFile.readlines()

for row in bookFile:
    column = row.split(",")
    ISBNN = column[0]
    Title = column[1]
    Author = column[2]
    Publisher = column[3]
    DatePublished = column[4]
    NumofPages = int(column[5])
    Price = column[6]

    if "Portfolio Hardcover" in Publisher:
        print(Title, Author, Publisher, DatePublished, NumofPages, Price)

bookFile.close()