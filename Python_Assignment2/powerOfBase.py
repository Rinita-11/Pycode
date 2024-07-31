def power(base, exponent):
    """Calculate base raised to the power of exponent using a loop."""
    result = 1
    for _ in range(exponent):
        result *= base
    return result
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
if exponent < 0:
    result = 1 / power(base, -exponent)
else:
    result = power(base, exponent)

print(f"{base} raised to the power of {exponent} is {result}.")
