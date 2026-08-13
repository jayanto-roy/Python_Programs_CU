# Program to reverse a number and check palindrome

number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)

if original == reverse:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")

# Program to reverse a number and check palindrome

number = input("Enter a number: ")

reverse = number[::-1]

print("Reversed number:", reverse)

if number == reverse:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")

# Program to reverse a text and check palindrome

text = input("Enter a text: ")

# Reverse the text
reverse = text[::-1]    #text[start:stop:step]

print("Reversed text:", reverse)

# Check palindrome
if text.capitalize() == reverse.capitalize():
    #lower() or capitalize() is used so that capital letters and small letters don't affect the palindrome check.
    print("The text is a Palindrome.")
else:
    print("The text is not a Palindrome.")


# MADAM → MADAM 
# LEVEL → LEVEL
# RADAR → RADAR
# MOM → MOM
# WOW → WOW
# NOON → NOON
# CIVIC → CIVIC
# REFER → REFER