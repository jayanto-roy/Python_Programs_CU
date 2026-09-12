text = "Python is Easy"

print("Original:", text)

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

words = text.split()
print("After split:", words)

joined = "-".join(words)
print("After join:", joined)

print("After replace:", text.replace("Easy", "Powerful"))