def num():
    n = int(input("Enter number : "))
    return n

def length(num):
    count = 0
    num = str(num)
    for char in num:
        count += 1
    return count

type = int(input("Select conversion type:\n1. Decimal to Binary\n2. Binary to Decimal\n3. Decimal to Octal\n4. Octal to Decimal\n5. Decimal to Hexadecimal\n6. Hexadecimal to Decimal\nEnter choice (1-6): "))

match type:
    case 1:
        rev = 0
        n = num()
        binary = ""
        while n > 0:
            rev = n % 2
            binary = str(rev) + binary
            n //= 2
        print("Binary :", binary)

    case 2:
        n = num()
        len = length(n)
        total = 0

        for i in range(0, len):
            while n > 0:
                new_num = n % 10
                if new_num == 1:
                    total += 2**i        
                n //= 10
                break
        print("Decimal :", total)

    case 3:
        n = num()
        octal = ""
        while n > 0:
            new_num = n % 8
            octal = str(new_num) + octal
            n //= 8
        print("Octal :", octal)
    
    case 4:
        n = num()
        total = 0
        len = length(n)

        for i in range(0, len):
            while n > 0:
                new_num = n % 10
                total += new_num * (8**i)
                n //= 10
                break
        print("Decimal :",total)

    case 5:
        n = num()
        hex = ""
        while n > 0:
            new_num = n % 16
            if new_num < 10:
                hex = str(new_num) + hex
            else:
                hex = chr(55 + new_num) + hex
            n //= 16
        print("HexaDecimal :", hex)

    case 6:
        n = num()      # hex number as string
        total = 0
        power = 0

        for ch in n[::-1]:
            if '0' <= ch <= '9':
                value = ord(ch) - 48
            else:
                value = ord(ch.upper()) - 55
            total += value * (16 ** power)
            power += 1

        print("Decimal :", total)

    case _:
        print("Enter valid number!")