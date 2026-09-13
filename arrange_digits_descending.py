# Question: Arrange the digits of a number in descending order.

import math
n = int(input())

ar = []
d = math.floor(math.log10(n)) 
    
while d >= 0:
    r = n//pow(10,d)
    ar.append(r)
    n = n%pow(10,d)
    d -= 1

ar.sort(reverse = True)
ans = 0
# for i in ar:  ans = ans*10 + i
for i in range(len(ar)):
    ans = ans * 10 + ar[i]

print(ans)

'''n = int(input("Enter a number: "))
ans = 0

for digit in range(9, -1, -1):
    temp = n
    
    while temp > 0:
        remainder = temp % 10
        if remainder == digit:
            ans = ans * 10 + digit 
        temp = temp // 10

print("Largest Number:", ans)'''
