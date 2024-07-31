def print_multiplication_table(number, up_to):
    print(f"Multiplication table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage:
number = int(input("Enter the number for which you want to generate the multiplication table: "))
up_to = int(input("Enter the range up to which you want the table: "))

print_multiplication_table(number, up_to)
