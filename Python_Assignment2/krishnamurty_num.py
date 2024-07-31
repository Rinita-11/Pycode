import math

def is_krishnamurthy_number(num):
    """Check if a number is a Krishnamurthy number."""
  
    num_str = str(num)

    sum_of_factorials = sum(math.factorial(int(digit)) for digit in num_str)
    return sum_of_factorials == num
number = int(input("Enter a number to check if it is a Krishnamurthy number: "))

if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
