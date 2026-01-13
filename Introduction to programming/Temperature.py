val = int(input("Select option : \n1. Centigrade to fahrenheit. \n2. Fahrenheit to centigrade \n"))

match val:
    case 1:
        c = int(input("Enter temperature in Centigrade :"))
        res = (c * (9/5)) + 32
        print("Fahrenheit :", res)
    case 2:
        f = int(input("Enter temperature in fahrenheit :"))
        res = (5 * (f-32)) / 9
        print("Centigrade :", res)
    case _:
        print("Invalid Option!")
