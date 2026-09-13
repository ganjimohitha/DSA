# Question: Find digits matching their positions.

import math

n = int(input())

if n == 0:
    ar = [0]
else:
    ar = []
    d = math.floor(math.log10(abs(n)))
    while d >= 0:
        r = n // (10 ** d)
        ar.append(r)
        n = n % (10 ** d)
        d -= 1

cnt = 0
for i in range(len(ar)):
    if ar[i] == len(ar) - 1 - i:
        print(f"{len(ar) - 1 - i} position is having number - {ar[i]}")
        cnt += 1

print(cnt)
