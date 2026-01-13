mat1 = [[1,2,3], [4,5,6]]
mat2 = [[0 for _ in range(2)] for _ in range(3)]

for i in range(3):
    for j in range(2):
        mat2[i][j] = mat1[j][i]
print(mat2)