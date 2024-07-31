def is_buzz_number(num):
    return num % 7 == 0 or num % 10 == 7
number = int(input("Enter a number: "))
if is_buzz_number(number):
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is not a Buzz number.")
