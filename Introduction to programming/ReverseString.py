n = input("Enter string : ")
# print(s[::-1])

count = 0
for i in n:
    count += 1
while count != 0:
    print(n[count-1], end='')
    count -= 1
 
# n = int(input("Enter number : "))
# while n > 0:
#     rev = n % 10
#     print(rev, end='')
#     n //= 10
