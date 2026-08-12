# Sum of first n natural numbers using while loop

n = int(input("Enter the value of n: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i += 1

print("Sum of first", n, "natural numbers is:", total)
