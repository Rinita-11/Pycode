def is_sparse_matrix(matrix):
    """Check if the given matrix is sparse."""
    total_elements = len(matrix) * len(matrix[0])
    zero_count = sum(1 for row in matrix for element in row if element == 0)
    return zero_count > total_elements / 2
matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
if is_sparse_matrix(matrix):
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")
