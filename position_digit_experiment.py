# Question: Check digit positions against their expected values.

n = int(input())
cnt = 0
for i in range(len(n)):
    if(ar[i] == len(n)-1-i):
        print(f"{len(n)-1-i} position is having number - {n[i]}")
        cnt += 1

print(cnt)
