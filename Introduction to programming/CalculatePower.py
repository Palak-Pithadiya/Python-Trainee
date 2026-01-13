def power(n, i):
    if i < 1:
        return 1
    else:
        return n * power(n, i-1)
    
print(power(2,4))