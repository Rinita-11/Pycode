def print_pattern():
    start = 1  
    rows = 3   

    for i in range(1, rows + 1):
        for j in range(2 * i - 1):
            print(start, end=" ")
            start += 1
        print()  
print_pattern()
