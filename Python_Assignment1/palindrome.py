def is_palindrome(n):
    # Convert the number to a string
    s = str(n)
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
number = 12321
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
