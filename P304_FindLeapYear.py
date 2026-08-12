# Program to check whether a year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("The year is a Leap Year.")
elif year % 100 == 0:
    print("The year is not a Leap Year.")
elif year % 4 == 0:
    print("The year is a Leap Year.")
else:
    print("The year is not a Leap Year.")
