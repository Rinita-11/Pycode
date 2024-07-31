import math

def compute_sine(x, n):
    """Compute sin(x) using the series expansion up to n terms."""
    sine_sum = 0
    sign = 1  
    
    for i in range(n):
        term_index = 2 * i + 1
        term = sign * (x ** term_index) / math.factorial(term_index)
        sine_sum += term
        sign *= -1
    
    return sine_sum
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

if n > 0:
    result = compute_sine(x, n)
    print(f"sin({x}) calculated using {n} terms is approximately {result}.")
else:
    print("Please enter a positive integer for the number of terms.")
