# Question: Find addition using recursion and iteration.

def sumi(a,b):
    if b == 0:
        return a
    
    ans = sumi(a,b-1) + 1
    return ans

a,b = map(int,input().split())
print(f"Addition : {sumi(a,b)}")

res = a
for i in range(1,b+1):
    res += 1
print(f"Result of iterative : {res}")
