# User-defined functions
# Positional arguments
def add(a, b):
    return a + b

# Default argument
def greet(name="Student"):
    print("Hello,", name)

# Variable-length arguments
def find_sum(*numbers):
    return sum(numbers)

# Calling positional argument function
result = add(10, 20)
print("Addition:", result)

# Calling default argument function
greet()
greet("Rahul")

# Calling variable-length argument function
total = find_sum(10, 20, 30, 40)
print("Sum using variable-length arguments:", total)
