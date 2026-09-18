import math

n = int(input())
mp = {}
for i in range(2,int(math.sqrt(n))+1):
    while(n%i == 0):
        print(i,end = " ")
        n //= i
        mp[i] = mp.get(i,0)+1

    if n == 1:
        break

if n > 1:
    print(n)
    mp[n] = 1

ans = 1
for i in mp.values():
    ans *= (i+1)

print("\n",ans)
