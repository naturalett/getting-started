import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
