# Demonstration of break statement

print("Break Statement:")

for i in range(1, 11):

    if i == 6:
        break

    print(i, end=" ")


# Demonstration of continue statement

print("\n\nContinue Statement:")

for i in range(1, 11):

    if i == 6:
        continue

    print(i, end=" ")


# Demonstration of pass statement

print("\n\nPass Statement:")

for i in range(1, 6):

    if i == 3:
        pass

    print(i, end=" ")
