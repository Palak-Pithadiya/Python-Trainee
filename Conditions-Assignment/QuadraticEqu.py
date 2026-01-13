a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d = (b*b) - 4*a*c

if d == 0:
    print("Roots are equal!")
elif d > 0:
    print("Roots are real!")
else:
    print("Roots are imaginary!")
