import csv
with open('names.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        print row
