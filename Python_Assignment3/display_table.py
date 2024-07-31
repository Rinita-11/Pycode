def print_table(rows):
    """Prints a table where each row displays an integer and its powers."""
    for i in range(1, rows + 1):
        row = [i ** j for j in range(5)]
        print(" ".join(map(str, row)))
num_rows = 5

print_table(num_rows)
