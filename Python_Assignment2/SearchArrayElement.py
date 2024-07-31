def linear_search(array, target):
    """Perform a linear search to find the target element in the array."""
    for index, element in enumerate(array):
        if element == target:
            return index  
    return -1  
array = [10, 5, 3, 8, 12, 7]
target = 8

index = linear_search(array, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
