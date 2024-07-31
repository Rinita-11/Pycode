def print_geometric_sequence(first_term, common_ratio, num_terms):
    """Print the first `num_terms` terms of a geometric sequence."""
    for n in range(num_terms):
        term = first_term * (common_ratio ** n)
        print(term)
first_term = 2
common_ratio = 3
num_terms = 6

print(f"First {num_terms} terms of the geometric sequence starting with {first_term} and common ratio {common_ratio}:")
print_geometric_sequence(first_term, common_ratio, num_terms)
