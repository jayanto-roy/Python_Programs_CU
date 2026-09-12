# Practical-09: String Operations

text = input("Enter a string: ")

print("\n----- STRING OPERATIONS -----")

# 1. Display original string
print("Original String :", text)

# 2. Length
print("Length          :", len(text))

# 3. Indexing
if len(text) > 0:
    print("First Character :", text[0])
    print("Last Character  :", text[-1])

# 4. Slicing
print("First 3 Chars   :", text[:3])
print("Last 3 Chars    :", text[-3:])
print("Reversed String :", text[::-1])

# 5. Concatenation
print("Concatenation   :", text + " Python")

# 6. Repetition
print("Repetition      :", text * 2)

# 7. String Methods
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("Title Case      :", text.title())
print("Capitalized     :", text.capitalize())
print("Stripped        :", text.strip())

# 8. Replace
old = input("\nEnter word/character to replace: ")
new = input("Enter new word/character: ")

print("After Replace   :", text.replace(old, new))

# 9. Split
words = text.split()
print("Split           :", words)

# 10. Join
print("Join            :", "-".join(words))

# 11. Find
search = input("\nEnter character/word to find: ")
print("Position        :", text.find(search))

# 12. Count
print("Occurrences     :", text.count(search))

# 13. Membership
print("Is Present?     :", search in text)

# 14. Character Traversal
print("\n----- CHARACTER TRAVERSAL -----")
for ch in text:
    print(ch)

# 15. Count vowels, consonants, digits and special characters
vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("\n----- CHARACTER COUNT -----")
print("Vowels          :", vowels)
print("Consonants      :", consonants)
print("Digits          :", digits)
print("Special Chars   :", special)

# 16. Palindrome
print("\n----- PALINDROME CHECK -----")

if text.lower() == text.lower()[::-1]:
    print("Palindrome      : Yes")
else:
    print("Palindrome      : No")

# 17. Check string contents
print("\n----- STRING CHECKING -----")
print("Only Alphabets  :", text.isalpha())
print("Only Digits     :", text.isdigit())
print("Alpha-Numeric   :", text.isalnum())
print("Lowercase       :", text.islower())
print("Uppercase       :", text.isupper())

print("\n----- PROGRAM COMPLETED -----")