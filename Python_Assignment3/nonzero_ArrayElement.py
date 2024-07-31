def count_non_zero_elements(array):
    """Count the number of non-zero elements in an integer array."""
    count = 0
    for element in array:
        if element != 0:
            count += 1
    return count
array = [0, 1, 0, 3, 5, 0, 7, 0, 9]
non_zero_count = count_non_zero_elements(array)
print(f"The number of non-zero elements in the array is {non_zero_count}.")
