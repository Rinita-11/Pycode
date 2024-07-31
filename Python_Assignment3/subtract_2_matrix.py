def subtract_matrices(matrix1, matrix2):
    """Subtract two matrices."""

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Both matrices must have the same dimensions.")
    result = [[0] * cols1 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols1):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result
matrix1 = [
    [10, 20, 30],
    [40, 50, 60]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
result_matrix = subtract_matrices(matrix1, matrix2)
print("Resulting matrix after subtraction:")
for row in result_matrix:
    print(row)
