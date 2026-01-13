def cube():
    a = float(input("Enter a :"))
    print("Volume of cube is :", a**3)

def cuboid():
    l = float(input("Enter l :"))
    b = float(input("Enter b :"))
    h = float(input("Enter h :"))
    print("Volume of cuboid is :", l*b*h)

def cylinder():
    r = float(input("Enter r :"))
    h = float(input("Enter h :"))
    print("Volume of cylinder is :", 3.14*(r**2)*h)

def cone():
    r = float(input("Enter r :"))
    h = float(input("Enter h :"))
    print("Volume of cone is :", (3.14*(r**2)*h)/3)

def sphere():
    r = float(input("Enter r :"))
    print("Volume of sphere is :", (4*3.14*(r**3))/3)

cone()
    