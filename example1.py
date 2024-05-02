def sum_matrix(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Sum of all numbers in matrix:", sum_matrix(matrix))