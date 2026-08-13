# Program to print Armstrong numbers between 1 and 1000

print("Armstrong numbers between 1 and 1000:")

for number in range(1, 1001):

    original = number
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit ** 3
        number = number // 10

    if total == original:
        print(original, end=" ")
