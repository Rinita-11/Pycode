def print_multiplication_table(number):
    """Print the multiplication table for the given number."""
    print(f"Multiplication table for {number}:")
    for i in range(1, 11): 
        print(f"{number} x {i} = {number * i}")


num = int(input("Enter a number to display its multiplication table: "))
print_multiplication_table(num)
