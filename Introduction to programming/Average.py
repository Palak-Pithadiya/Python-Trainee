count = 0
n = 5
print("Enter 5 subjects marks :-")
for i in range(1, n+1):
    sub = int(input(f"Enter {i} subject marks : "))
    count += sub
print("Average : ", count/n)
