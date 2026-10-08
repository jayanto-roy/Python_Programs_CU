file = open("student.txt", "r")

content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Number of Characters:", characters)

file.close()