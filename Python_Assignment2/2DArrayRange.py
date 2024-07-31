def find_range(array):
    """Calculate the range of a 1D array."""
    if not array:  
        raise ValueError("Array is empty")
    
    min_value = min(array)
    max_value = max(array)
    
    return max_value - min_value
array = [10, 5, 3, 8, 12, 7]
range_value = find_range(array)
print(f"The range of the array is {range_value}.")
