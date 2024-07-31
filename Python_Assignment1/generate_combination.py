def generate_combinations():
    numbers = [1, 2, 3]
    combinations = []
    for i in numbers:
        combinations.append([i])  
        for j in numbers:
            combinations.append([i, j])  
            for k in numbers:
                combinations.append([i, j, k])   

    return combinations
combinations = generate_combinations()
print("All combinations of 1, 2, and 3 are:")
for combo in combinations:
    print(combo)
