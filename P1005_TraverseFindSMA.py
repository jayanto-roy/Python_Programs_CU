numbers = [10, 20, 30, 40, 50]

total = 0

print("List elements:")

for number in numbers:
    print(number)
    total = total + number

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))