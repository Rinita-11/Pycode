def reverse_string(s):
    """Return the reverse of the given string."""
    return s[::-1]
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")
