def find_smallest_number(array):
    """Find the smallest number in the array."""
    if not array:
        raise ValueError("Array is empty")
    
    smallest = array[0]
    for num in array[1:]:
        if num < smallest:
            smallest = num
    return smallest
n = int(input("Enter the number of elements: "))
array = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
smallest_number = find_smallest_number(array)
print(f"The smallest number in the array is {smallest_number}.")
