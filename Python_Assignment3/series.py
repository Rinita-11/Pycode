def compute_series_sum(n):
    """Compute the sum of the series 1 - 1/2 + 1/3 - 1/4 + ... ± 1/n."""
    series_sum = 0
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            series_sum -= 1 / i
        else:
            series_sum += 1 / i
    
    return series_sum
n = int(input("Enter the number of terms (n): "))
if n > 0:
    result = compute_series_sum(n)
    print(f"The sum of the series up to {n} terms is {result}.")
else:
    print("Please enter a positive integer for n.")
