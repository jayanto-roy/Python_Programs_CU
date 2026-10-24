# Practical 1: Common Elements in Two Lists
list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80]
common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common)