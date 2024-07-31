def find_numbers():
    results = []
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            results.append(num)
    return results

# Example usage:
numbers = find_numbers()
print("Numbers between 1000 and 2000 that are divisible by 7 but not multiples of 5:")
print(numbers)
