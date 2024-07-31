def transpose_matrix(matrix):
    """Compute the transpose of a matrix."""
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def print_matrix(matrix):
    """Prints a matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose_matrix(matrix)
print("Original matrix:")
print_matrix(matrix)
print("\nTransposed matrix:")
print_matrix(transposed_matrix)
