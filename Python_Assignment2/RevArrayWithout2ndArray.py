def reverse_array(arr):
    """Reverse the elements of the array in place."""
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
array = [1, 2, 3, 4, 5]

print("Original array:", array)
reverse_array(array)

print("Reversed array:", array)
