
def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


# Main program
numbers = [5, 2, 8, 1, 3]

print("Original list:", numbers)

result = bubble_sort(numbers)

print("Sorted list:", result)
