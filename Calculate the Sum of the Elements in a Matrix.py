matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum_of_elements = sum(sum(row) for row in matrix)
print("Sum of the elements in the matrix is", sum_of_elements)
