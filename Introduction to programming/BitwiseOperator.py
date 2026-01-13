# Left shift : 3 << 2 => 12
# Right shift : 16 >> 2 => 4

def leftShift(a, n):
    return a * (2**n)
def rightShift(a, n):
    return a // (2**n)

print(leftShift(3, 2))
print(rightShift(16, 2))
