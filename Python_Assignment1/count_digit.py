def count_digits(n):
    # Convert the integer to a string and strip out any negative sign
    return len(str(abs(n)))

# Example usage:
number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is {digit_count}.")
