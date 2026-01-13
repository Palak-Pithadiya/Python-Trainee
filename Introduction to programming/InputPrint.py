# Write a program in c to input and print details of an employee the id,name,salary using structure.

employee = []

def inputData():
    emp = {}
    emp["Id"] = int(input("Enter ID: "))
    emp["Name"] = input("Enter name : ")
    emp["Salary"] = int(input("Enter salary : "))

    employee.append(emp)
    
n = int(input("How many employee data you want to add? :"))

for _ in range(n):
    inputData()

for i in range(n):
    print(employee[i])