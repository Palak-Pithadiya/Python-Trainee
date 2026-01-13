lst = [10, 20, 30, 40, 50]
print(lst)
n = int(input("Enter the element you want to search :"))

for i in range(len(lst)):
    if n == lst[i]:
        print(f"Element found at {i} index.")
        break
print("Element not Found!")