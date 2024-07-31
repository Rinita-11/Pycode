def sum_of_odd_numbers(matrix):
    """Calculate the sum of all odd numbers in a 2D array."""
    total_sum = 0
    
    for row in matrix:
        for element in row:
            if element % 2 != 0:
                total_sum += element
                
    return total_sum
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = sum_of_odd_numbers(array)
print(f"The sum of all odd numbers in the 2D array is {result}.")
