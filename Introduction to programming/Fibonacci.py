n = int(input("Enter range : "))
n1 = 0
n2 = 1
i = 1

print(n1, end=" ")

while i < n:
    print(n2, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1