def power(base, exponent):
    """Calculate the power of a number using recursion."""
 
    if exponent == 0:
        return 1
   
    elif exponent > 0:
        return base * power(base, exponent - 1)
 
    elif exponent < 0:
        return 1 / power(base, -exponent)
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}.")
