matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

primary_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
secondary_diagonal_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))

print("Sum of the primary diagonal:", primary_diagonal_sum)
print("Sum of the secondary diagonal:", secondary_diagonal_sum)
