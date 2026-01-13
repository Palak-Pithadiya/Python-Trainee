n1 = int(input("Enter angle-1 :"))
n2 = int(input("Enter angle-2 :"))
n3 = int(input("Enter angle-3 :"))

total = n1+n2+n3

if total == 180:
    print("Triangle is valid!")
else:
    print("Triangle is not valid!")