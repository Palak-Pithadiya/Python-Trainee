print("\nDecimal :")
for i in range(1, 11):
    print(i, end=' ') 

print("\n\nOctal :")
for i in range(1, 11):
    j = 0
    octal = ''
    while i > 0:
        temp = i % 8
        octal = str(temp) + octal
        i //= 8
        j += 1
    print(octal, end=' ')         

print("\n\nHexaDecimal :")
for i in range(1, 11):
    j = 0
    hex = ''
    while i > 0:
        temp = i % 16
        if i < 10:
            hex = str(temp) + hex
        else:
            hex = chr(temp+ 55) + hex
        i //= 16
        j += 1
    print(hex, end=' ')
