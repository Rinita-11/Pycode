def check_odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Example usage:
number = 7
result = check_odd_or_even(number)
print(f"The number {number} is {result}.")
