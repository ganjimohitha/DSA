# Question: Check whether three sides form a triangle.

a,b,c = map(int,input().split())

if a+b>c or b+c>a or c+a>b:
    print("Traingle")
else:
    print("Not an Triangle")
