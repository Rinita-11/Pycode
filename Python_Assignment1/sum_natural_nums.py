def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# Example usage:
n = int(input("Enter the range up to which you want to sum natural numbers: "))
sum_result = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is {sum_result}.")
