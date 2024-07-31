def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def display_primes(start, end):
    """Display all prime numbers in the given interval [start, end]."""
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

display_primes(start, end)
