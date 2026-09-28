employees = {}

while True:
    print("\n ---- Employee Management System----")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Emplyee")
    print("4. Diplay Employees")
    print("5. Exit")

    choice = int(input("Enter your Choice : "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input(("Enter Employee Name: "))
        salary = float(input("ENter Salary: "))

        employees[emp_id] = {
            "Name" : name,
            "Salary" : salary,
        }

        print("Employee added successfully.")

    elif choice == 2:
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees: 
            salary = float(input("Enter new salary: "))
            employees[emp_id]["Salary"] = salary
            print("Salary updated successfully.")

        else: 
            print("Employee not found.")

    elif choice == 3:
        emp_id = input("Enter Empoloyee ID: ")

        if emp_id in employees: 
            del employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee ont found.")

    elif choice == 4:
        print("\nEmployee Details:")

        for key, value in employees.items():
            print(key, ":", value)

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid Choice!")



