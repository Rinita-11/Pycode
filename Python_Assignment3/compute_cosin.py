import math

def compute_cosine(x, n):
    """Compute cos(x) using the series expansion up to n terms."""
    cosine_sum = 0
    sign = 1  
    
    for i in range(n):
        term_index = 2 * i
        term = sign * (x ** term_index) / math.factorial(term_index)
        cosine_sum += term
        sign *= -1
    
    return cosine_sum
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

if n > 0:
    result = compute_cosine(x, n)
    print(f"cos({x}) calculated using {n} terms is approximately {result}.")
else:
    print("Please enter a positive integer for the number of terms.")
