
import math

# Function to calculate area of circle
def circle(r):
    return math.pi * r * r

# Function to calculate area of triangle
def triangle(b, h):
    return 0.5 * b * h

# Function to calculate area of rectangle
def rectangle(l, w):
    return l * w

# Function to calculate area of square
def square(s):
    return s * s

# Function to calculate volume of cube
def cube(s):
    return s * s * s


# Menu-driven program
while True:
    print("\n--- MENU ---")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Rectangle")
    print("4. Area of Square")
    print("5. Volume of Cube")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        print("Area of Circle =", round(circle(r), 2))

    elif choice == "2":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of Triangle =", triangle(b, h))

    elif choice == "3":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of Rectangle =", rectangle(l, w))

    elif choice == "4":
        s = float(input("Enter side: "))
        print("Area of Square =", square(s))

    elif choice == "5":
        s = float(input("Enter side of cube: "))
        print("Volume of Cube =", cube(s))

    elif choice == "6":
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")