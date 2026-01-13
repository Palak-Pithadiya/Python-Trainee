s = input("Enter string :")
upper = ''
lower = ''
num = ''
special = ''

for char in s:
    if '0' <= char <= '9':
        num += char
    elif "A" <= char <= "Z":
        upper += char
    elif 'a' <= char <= 'z':
        lower += char
    else:
        special += char

print("Uppercase Text :", upper)
print("Lowercase Text :", lower)
print("Numbers are :", num)
print("Special characters are :", special)