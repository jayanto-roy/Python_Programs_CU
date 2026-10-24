
# Practical 3: Palindrome String

text = input("Enter a string: ")

# Remove spaces and convert to lowercase
clean_text = text.replace(" ", "").lower()

# Reverse the string
reverse_text = clean_text[::-1]

if clean_text == reverse_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
