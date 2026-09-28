emp = {}

# Add
emp["E101"] = {"Name": "Rahul", "Salary": 25000}

# Update salary
emp["E101"]["Salary"] = 30000

# Add another employee
emp["E102"] = {"Name": "Aman", "Salary": 28000}

# Delete
del emp["E102"]

# Display
for key, value in emp.items():
    print(key, ":", value)