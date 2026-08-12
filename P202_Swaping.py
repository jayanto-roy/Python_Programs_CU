# Taking input
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
# Swapping with temporary variable
x = a
y = b
temp = x
x = y
y = temp
print("\nAfter swapping using temporary variable:")
print("A =", x)
print("B =", y)
# Swapping without temporary variable
x = a
y = b
x, y = y, x
print("\nAfter swapping without temporary variable:")
print("A =", x)
print("B =", y)
