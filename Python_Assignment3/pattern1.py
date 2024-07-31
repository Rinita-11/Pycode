def print_pattern(n):
    """Print the specified pattern up to n lines."""
    for i in range(1, n + 1):
        print('/' + '_' * (2 * i - 1) + '\\')
        for j in range(i):
            print('/' + ' ' * (2 * j + 1) + '\\')
n = int(input("Enter the number of lines (N): "))

if n > 0:
    print_pattern(n)
else:
    print("Please enter a positive integer for the number of lines.")
