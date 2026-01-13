n = int(input("Enter number : "))
is_prime = True

if n<=1:
    is_prime = False

for i in range(2, n):
    if n%i == 0:
        is_prime = False
        break

if is_prime:
    print("True")
else:
    print("False")