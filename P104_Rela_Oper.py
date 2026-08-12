# Taking marks from the user

marks = float(input("Enter your marks: "))

# Relational and logical operators

if marks >= 40 and marks <= 100:
    print("Result: Pass")
elif marks >= 0 and marks < 40:
    print("Result: Fail")
else:
    print("Invalid marks!")

# Demonstrating relational operators

print("\nRelational Operators:")
print("Marks >= 40:", marks >= 40)
print("Marks < 40:", marks < 40)
print("Marks == 100:", marks == 100)
print("Marks != 50:", marks != 50)

# Demonstrating logical operators

print("\nLogical Operators:")
print("Marks >= 40 and marks <= 100:", marks >= 40 and marks <= 100)
print("Marks < 40 or marks == 100:", marks < 40 or marks == 100)
print("not(marks < 40):", not(marks < 40))
