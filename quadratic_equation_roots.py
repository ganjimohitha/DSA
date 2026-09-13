# Question: Find the roots of a quadratic equation.

import math
a,b,c = map(int,input().split())

dis = b ** 2 - 4*a*c
if dis < 0:
    print("Imaginary Roots")
elif dis == 0:
    print("Equal Roots",-b/(2*a))
else:
    root1 = (-b + math.sqrt(dis)) /(2*a)
    root2 = (-b - math.sqrt(dis)) /(2*a)
    print(f"Root1 = {root1} and Root2 = {root2}")
