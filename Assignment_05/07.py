# Write a Python program that transposes a given 2D list (matrix) by converting its rows into columns and columns into rows.

def transpose_matrix(matrix):
    transposed_matrix = []
    for col in range(len(matrix[0])):
        transposed_row = []
        for row in range(len(matrix)):
            transposed_row.append(matrix[row][col])
        transposed_matrix.append(transposed_row)
    return transposed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
