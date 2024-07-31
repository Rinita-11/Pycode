def check_number_sign(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# Example usage:
number = 7
result = check_number_sign(number)
print(f"The number {number} is {result}.")
