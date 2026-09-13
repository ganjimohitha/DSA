# Question: Check whether a number is an automorphic number.

import math
n = int(input())
sq = n**2

'''d = math.floor(math.log10(n))+1
if sq%math.pow(10,d) == n:
    print("Yes",sq)
else:
    print("No",sq)'''

'''temp = sq
flag = 1
while(n > 0):
    if n%10 == sq%10:
        n //= 10
        sq //= 10
    else:
        flag = 0
        break

if flag:
    print("Yes",temp)
else:
    print("NO",temp) '''

if str(sq).endswith(str(n)):
    print("Yes",sq)
else:
    print("No",sq)
