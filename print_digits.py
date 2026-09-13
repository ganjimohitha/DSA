# Question: Print the digits of a number.

import math

n = int(input())
d = math.floor(math.log10(abs(n)))

while d >= 0:
    r = n // (10 ** d)
    print(r, end=" ")

    n = n % (10 ** d)
    d -= 1
