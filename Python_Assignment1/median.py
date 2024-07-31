def find_median(numbers):
    numbers.sort() 
    n = len(numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
median_result = find_median(numbers)
print(f"The median is {median_result}.")
