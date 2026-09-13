# Question: Create functions to wish a user and find the sum of two numbers.

def wish(name):
    print(f"Hi {name} , How are you ??")    

def sumi(a,b):
    return (a+b)

s = input()
wish(s)

a,b = map(int,input().split())
x = sumi(a,b)
print(f"sum = {x}")
