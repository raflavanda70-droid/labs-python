def transpose_matrix(matrix):

    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


print("Введите матрицу (числа через пробел, пустая строка - конец):")
matrix = []
while True:
    row_input = input().strip()
    if not row_input:
        break
    matrix.append([int(x) for x in row_input.split()])

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(str(x) for x in row))


result = transpose_matrix(matrix)
print("\nТранспонированная матрица:")
for row in result:
    print(" ".join(str(x) for x in row))