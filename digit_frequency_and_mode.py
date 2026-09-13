# Question: Find digit frequency, mode, unique digits and duplicate digits.

n = int(input())

ar = [0]*10
while(n > 0):
    r = n%10
    ar[r] += 1
    n = n//10

ans = -1
max_cnt = -1
for i in range(len(ar)):
    if(ar[i] > max_cnt):
        max_cnt = ar[i]
        ans = i
print("Mode: ",ans)

print("Unique Digit: ",end ="")
for i in range(len(ar)):
     if(ar[i] == 1):
        print(f"{i} ",end = "")

print()
print("Duplicate Digits: ",end="")
for i in range(len(ar)):
    if(ar[i] > 1):
        print(f"{i} ",end = "")
