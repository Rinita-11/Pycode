def print_multiples_of_10(start, end):
    # Find the first multiple of 10 greater than or equal to start
    if start % 10 == 0:
        first_multiple = start
    else:
        first_multiple = start + (10 - start % 10)
    
    # Print all multiples of 10 from first_multiple to end
    for number in range(first_multiple, end + 1, 10):
        print(number)

# Example usage:
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Multiples of 10 between {start} and {end} are:")
print_multiples_of_10(start, end)
