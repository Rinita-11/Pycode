import math

def compute_euler_number(n):
    e = 1.0  
    factorial = 1  
    
    for i in range(1, n + 1):
        factorial *= i  
        e += 1 / factorial  
    
    return e
n = int(input("Enter the number of terms to compute Euler's number: "))
euler_number = compute_euler_number(n)
print(f"Euler's number computed with {n} terms is approximately {euler_number}.")
