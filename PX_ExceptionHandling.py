
try:
    # TypeError
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a + b
    print("Sum =", result)

except TypeError:
    print("TypeError: Invalid data types.")

except ValueError:
    print("ValueError: Please enter integers only.")


# try:
#     # IOError
#     filename = input("\nEnter file name to open: ")
#     file = open(filename, "r")
#     print(file.read())
#     file.close()

# except IOError:
#     print("IOError: File not found or cannot be opened.")

# try:
#     # NameError
#     print(undefined_variable)

# except NameError:
#     print("NameError: Variable is not defined.")

# try:
#     # KeyError
#     student = {"name": "Rahul", "age": 20}
#     key = input("\nEnter dictionary key (name/age/course): ")
#     print(student[key])

# except KeyError:
#     print("KeyError: Key does not exist.")

# try:
#     # ValueError
#     number = int(input("\nEnter an integer: "))
#     print("Number =", number)

# except ValueError:
#     print("ValueError: Invalid integer value.")