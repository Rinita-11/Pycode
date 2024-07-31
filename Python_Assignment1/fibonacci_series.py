def fibonacci_series_up_to(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series

# Example usage:
n = 100
fib_series = fibonacci_series_up_to(n)
print(f"Fibonacci series up to {n}: {fib_series}")
