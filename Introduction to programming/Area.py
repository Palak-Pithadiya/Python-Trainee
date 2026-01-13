# circle, square, ractangle

print("1. Area of Circle \n2. Area of Square \n3. Area of Ractangle")
case = int(input("Selct option : "))

match case:
    case 1:
        r = int(input("Enter radius : "))
        print("Area of circle is :", 3.14*2*r)
    case 2:
        l = int(input("Enter length : "))
        print("Area of square is :", l*l)
    case 3:
        l = int(input("Enter length : "))
        b = int(input("Enter bridth : "))
        print("Area of rectangle is :", l*b)
    case _:
        print("Enter valis option!")
