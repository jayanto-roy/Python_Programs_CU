# Program to check whether a number is prime or not

number = int(input("Enter a number: "))

if number <= 1:
    print("The number is not a Prime Number.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is a Prime Number.")
    else:
        print("The number is not a Prime Number.")
