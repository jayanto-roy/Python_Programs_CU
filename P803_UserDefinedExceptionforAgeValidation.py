# User-defined exception for age validation

class InvalidAgeError(Exception):
    pass


def validate_age(age):

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    else:
        print("Age is valid.")


try:

    age = int(input("Enter your age: "))

    validate_age(age)

except InvalidAgeError as e:

    print("Invalid Age:", e)

except ValueError:

    print("Error: Please enter a valid number.")