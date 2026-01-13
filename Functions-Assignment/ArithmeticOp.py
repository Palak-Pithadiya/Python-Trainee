def arithmeticOp(n1, n2, op):
    if op == "+":
        return f"n1 + n2 = {n1+n2}"
    if op == "-":
        return f"n1 - n2 = {n1-n2}"
    if op == "*":
        return f"n1 * n2 = {n1*n2}"
    if op == "/":
        return f"n1 / n2 = {n1/n2}"

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
op = input("Enter Operation(+, -, *, /) : ")
print(arithmeticOp(n1, n2, op))