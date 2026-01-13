def mat(r, c):
    val = []
    for i in range(r):
        raw = []
        for j in range(c):
            raw.append(int(input(f"Enter value[{i}][{j}] : ")))
        val.append(raw)
        print()
    return val


print("--Matrix 1--")
r1 = int(input("How many rows you want? : "))
c1 = int(input("How many columns you want? : "))
mat1 = mat(r1, c1)

print("--Matrix 2--")
r2 = int(input("How many rows you want? : "))
c2 = int(input("How many columns you want? : "))
mat2 = mat(r2, c2)

if(c1 == r2):
    for i in range(r1):
        for j in range(c2):
            result = 0
            for k in range(c1):
                result += mat1[i][k] * mat2[k][j]
            print(result, end=' ')
        print()
else:
    print("ERROR:_Matrix multiplication not possible")