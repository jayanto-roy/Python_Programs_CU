import math

print("----- Area Calculation -----")

# Circle
radius = float(input("Enter radius of circle: "))
circle_area = math.pi * radius ** 2

# Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rectangle_area = length * breadth

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height

print("\nArea of Circle:", circle_area)
print("Area of Rectangle:", rectangle_area)
print("Area of Triangle:", triangle_area)
