student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}

# a) get()
print("get():", student.get("name"))

# b) keys()
print("keys():", student.keys())

# c) pop()
print("pop():", student.pop("age"))

# d) update()
student.update({"branch": "IT"})
print("update():", student)

# e) values()
print("values():", student.values())

# f) items()
print("items():", student.items())