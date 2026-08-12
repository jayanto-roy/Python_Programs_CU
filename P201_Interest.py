# Program to calculate Simple and Compound Interest
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (in years): "))
# Simple Interest
si = (p * r * t) / 100
# Compound Interest
amount = p * (1 + r / 100) ** t
ci = amount - p
print("\nSimple Interest:", si)
print("Compound Interest:", ci)
print("Total Amount after Compound Interest:", amount)
