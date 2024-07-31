def calculate_sum_and_average(numbers):
    """Calculate the sum and average of an integer array."""
    total_sum = sum(numbers)  
    count = len(numbers)  
    
    if count == 0:
        average = 0  
    else:
        average = total_sum / count  
    
    return total_sum, average
input_string = input("Enter integers separated by spaces: ")
input_list = list(map(int, input_string.split()))
total_sum, average = calculate_sum_and_average(input_list)

print(f"Sum of the array elements is: {total_sum}")
print(f"Average of the array elements is: {average}")
