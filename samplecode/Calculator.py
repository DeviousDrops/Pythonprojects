def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

operations={
    '+':add,
    '-':sub,
    '*':mult,
    '/':div
    }

p=int(input("Enter the first number"))
q=int(input("Enter the second number"))
for i in operations:
    print(i)
op=input("Enter the operation to be performed")
calc=operations[op]
ans=calc(p,q)
print(f"{p} {op} {q} = {ans}")

while True:
    s=input("Do u want to perform another operation? Type y/n...")
    if s=='n':
        break
    c=int(input('Enter another number to perform an operation'))
    for i in operations:
        print(i)
    op=input("Enter the operation to be performed")
    calc=operations[op]
    temp=ans
    ans=calc(ans,c)
    print(f"{temp} {op} {c} = {ans}")