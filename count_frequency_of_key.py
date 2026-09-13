# Question: Count the frequency of a key in an array.

def fact(n):
    if n == 0 or n == 1:
        return 1

    ans = n*fact(n-1)
    return ans
    
num = int(input())
sum = 0
for i in range(1,num+1):
    sum += i*(1/fact(i))
    if i != num:
        print(f"{i}/{i}! + ", end = " ")
    else:
        print(f"{i}/{i}!",end = " ")
    
print(f" = {sum}")
