import csv
a="amazon"     #String that you want to search
with open("stocks.csv") as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:      #Iterates through the rows of your csv
               #line here refers to a row in the csv
        if a in str(line):      #If the string you want to search is in the row
            print("String found in first row of csv")
            print(type(line))
            print (line[0])
        else:
            continue