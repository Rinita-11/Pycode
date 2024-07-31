import math

def print_factorial_series(n):
    """Print the first `n` terms of the factorial series."""
    for i in range(1, n + 1):
        term = math.factorial(i)
        print(term, end=", " if i < n else "\n")
num_terms = int(input("Enter the number of terms to print in the series: "))
print(f"First {num_terms} terms of the factorial series:")
print_factorial_series(num_terms)
