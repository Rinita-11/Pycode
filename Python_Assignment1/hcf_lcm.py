import math

def find_hcf(a, b):
    return math.gcd(a, b)

def find_lcm(a, b):
    return abs(a * b) // find_hcf(a, b)

# Example usage:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

hcf = find_hcf(a, b)
lcm = find_lcm(a, b)

print(f"The HCF of {a} and {b} is {hcf}.")
print(f"The LCM of {a} and {b} is {lcm}.")
