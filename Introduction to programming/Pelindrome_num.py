n = int(input("Enter number : "))
rev = 0
temp = n

while n > 0:
    rev = (rev*10) + (n%10)
    n = n//10

if rev == temp:
    print("True")
else:
    print("False") 