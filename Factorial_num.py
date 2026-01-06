n = int(input("Enter number : "))

fact = 1
for i in range(1, n+1):
    fact *= i

print("Without using recursion :", fact)

# Using recursion

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
print("With using recursion :",factorial(n))