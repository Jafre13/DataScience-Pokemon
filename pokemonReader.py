import csv;

file = open("pokemon.csv",newline="");
reader = csv.reader(file)
for row in reader:
    print(row[0])