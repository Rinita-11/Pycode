def add_arrays(array1, array2):
    """Add elements of two integer arrays index-wise and store in a third array."""
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same length.")
    result = [0] * len(array1)
    for i in range(len(array1)):
        result[i] = array1[i] + array2[i]
    
    return result
array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
result_array = add_arrays(array1, array2)
print("Resulting array after addition:", result_array)
