import csv

file = open("Students.csv", "r")

reader = csv.reader(file)

for row in reader:
    print("{:<10} {:<15} {:<10} {:<10}".format(
        row[0], row[1], row[2], row[3]
    ))

file.close()