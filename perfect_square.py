# Question: Check whether a number is a perfect square.

import math
n = int(input())

x = round(n**(1/2))
if n == math.pow(x,2):
    print("Yes, it is an perfect square")
else :
    print("No, it is not a perfect sqaure")


'''sr = int(input())

x = round(n**(1/sr))
if n == math.pow(x,sr):
    print("Yes it is")
else :
    print("No")'''
