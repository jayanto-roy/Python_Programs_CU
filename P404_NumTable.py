# Multiplication table using for loop

number = int(input("Enter a number: "))

print("\nMultiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
