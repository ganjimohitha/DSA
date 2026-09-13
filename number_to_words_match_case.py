# Question: Convert a number into words digit by digit using match case.

import math
n = int(input())

d = math.floor(math.log10(abs(n)))
d1 = len(str(abs(n)))
print(d1)
print(d)
while (d >= 0):
        r = n // 10 ** d # 345/100 --> qouient (3)
        n = n % 10 ** d # 345%10 --> rem (45)
        d -= 1
    
        match r:
            case 1:
                print("One",end = " ")
            case 2:
                print("Two",end = " ")
            case 3:
                print("Three",end = " ")
            case 4:
                print("Four",end = " ")
            case 5:
                print("Five",end = " ")
            case 6:
                print("Six",end = " ")
            case 7:
                print("Seven",end = " ")
            case 8:
                print("Eight",end = " ")
            case 9:
                print("Nine",end = " ")
            case 0:
                print("Zero",end = " ")
            case _:
                print("Invalid")
