def is_armstrong_number(n):
    s = str(n)
    num_digits = len(s)
    sum_of_powers = sum(int(digit) ** num_digits for digit in s)
    return sum_of_powers == n

# Example usage:
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
