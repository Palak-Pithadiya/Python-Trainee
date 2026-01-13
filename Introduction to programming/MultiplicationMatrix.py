mat1 = [[1,2,3], [1,2,3]]
mat2 = [[1,2], [2,3], [1,2]]

for i in range(2):
    for j in range(2):
        result = 0
        for k in range(3):
            result += mat1[i][k] * mat2[k][j]
        print(result, end=' ')
    print()