def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

# Example usage:
# Convert Binary to Decimal
binary_str = input("Enter a binary number: ")
decimal_result = binary_to_decimal(binary_str)
print(f"The decimal equivalent of binary {binary_str} is {decimal_result}.")

# Convert Decimal to Binary
decimal_num = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_num)
print(f"The binary equivalent of decimal {decimal_num} is {binary_result}.")
