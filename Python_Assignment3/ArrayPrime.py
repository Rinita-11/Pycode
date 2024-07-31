import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(array):
    """Count the number of prime numbers in an array."""
    return sum(1 for x in array if is_prime(x))
array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19]
prime_count = count_primes(array)
print(f"The number of prime numbers in the array is {prime_count}.")
