def find_second_highest(array):
    """Find the second highest element in an array."""
    if len(array) < 2:
        raise ValueError("Array must contain at least two elements.")

    highest = second_highest = float('-inf')
    
    for num in array:
        if num > highest:
            second_highest = highest
            highest = num
        elif highest > num > second_highest:
            second_highest = num
    
    if second_highest == float('-inf'):
        raise ValueError("There is no distinct second highest element.")
    
    return second_highest
array = [10, 20, 4, 45, 99, 100]
try:
    second_highest = find_second_highest(array)
    print(f"The second highest element in the array is {second_highest}.")
except ValueError as e:
    print(e)
