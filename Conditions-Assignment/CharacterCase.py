# Write a C program to check whether a character is uppercase or lowercase alphabet
ch = input()

if 'A' <= ch <= 'Z':
    print("Uppercase alphabet")
elif 'a' <= ch <= 'z':
    print("Lowercase alphabet")
else:
    print("Not an alphabet")