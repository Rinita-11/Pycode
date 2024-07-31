import math

def sum_of_square_roots(a, b, c):
    return math.sqrt(a) + math.sqrt(b) + math.sqrt(c)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

total = sum_of_square_roots(num1, num2, num3)
print(f"The sum of the square roots is {total}.")
