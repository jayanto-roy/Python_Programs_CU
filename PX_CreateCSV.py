
import csv

# Create country data
countries = [
    ["Country", "Matches Won"],
    ["India", 5],
    ["Australia", 4],
    ["England", 3],
    ["Bangladesh", 2]
]

# Write data to CSV file
with open("countries.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(countries)

print("CSV file created successfully!")

# Read and display the CSV file
with open("countries.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)





        
# Create country data
countries = [
    ("India", 5),
    ("Australia", 4),
    ("England", 3),
    ("Bangladesh", 2)
]

# Create and write data to TXT file
with open("countries.txt", "w") as file:
    file.write("Country\tMatches Won\n")

    for country, matches in countries:
        file.write(f"{country}\t\t{matches}\n")

print("TXT file created successfully!")

# Read and display the TXT file
with open("countries.txt", "r") as file:
    print(file.read())