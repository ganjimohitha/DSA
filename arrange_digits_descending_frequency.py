# Question: Arrange the digits of a number in descending order using digit frequency.

n = int(input())
ar = [0]*10

while n > 0:
    r = n%10
    ar[r] += 1
    n = n//10

ans = 0
for i in range(len(ar)-1,-1,-1):
    if ar[i] != 0:
        while(ar[i] != 0):
            ans = ans*10 + i
            ar[i] -= 1

print(ans)
