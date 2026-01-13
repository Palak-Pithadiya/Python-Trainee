c = input("Enter character : ")

if len(c) != 1:
    print("Invalid input!")
elif c.isdigit():
    print("Character is digit!")
elif c.isalpha():
    print("Character is alphabet!")
else:
    print("Character is special character!")