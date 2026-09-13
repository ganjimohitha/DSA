# Question: Check whether a number is a perfect cube.

n = int(input())


'''for i in range(1,n//3+1):
    if i**3 == n:
        print("YES")
        break

else:
    print("NO")'''

x = round(n ** (1/3))
if x**3 == n:
    print("yes")
else:
    print("NO")
