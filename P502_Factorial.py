# Program to find factorial of a number

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "is:", factorial)
