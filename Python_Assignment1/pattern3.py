def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (2 * (i - 1)), end="")
        print(i, end=" ")
        if i != n:
            print("  " * (2 * (n - i - 1)), end=" ")
            print(i, end="")

        print()  
rows = 4  
print_pattern(rows)
