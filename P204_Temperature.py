print("----- Temperature Conversion -----")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Fahrenheit to Celsius
fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))

celsius_result = (fahrenheit_input - 32) * 5 / 9

print("Temperature in Celsius:", celsius_result)
