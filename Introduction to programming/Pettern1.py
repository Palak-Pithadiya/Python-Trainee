s = 'ABCDEFGHIJKLMNO'
n = len(s)
print(s)
m = n//2 + 1

for i in range(1, m):
    temp = m - i
    print(s[:temp] + " "*(n - temp*2) + s[n-temp:])