def sum_of_even_numbers(array):
    """Calculate the sum of even numbers in the array."""
    total_sum = 0
    for num in array:
        if num % 2 == 0:  
            total_sum += num
    return total_sum


array = [10, 15, 22, 33, 40, 55, 60]  
even_sum = sum_of_even_numbers(array)
print(f"The sum of even numbers in the array is {even_sum}.")
