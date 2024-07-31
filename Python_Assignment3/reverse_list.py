def reverse_list(arr):
    """Returns a new list which is the reverse of the input list."""
    reversed_arr = []
    length = len(arr)
    
    for i in range(length - 1, -1, -1):
        reversed_arr.append(arr[i])
    
    return reversed_arr
example_array = [1, 2, 3, 4, 5]
reversed_array = reverse_list(example_array)
print("Reversed array:", reversed_array)
