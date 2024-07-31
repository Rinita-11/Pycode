def check_multiple(m, n):
    if n == 0:
        return "Division by zero is not allowed."
    elif m % n == 0:
        return f"{m} is a multiple of {n}."
    else:
        return f"{m} is not a multiple of {n}."
m = int(input("Enter the first integer (m): "))
n = int(input("Enter the second integer (n): "))

result = check_multiple(m, n)
print(result)
