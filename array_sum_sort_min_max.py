# Question: Find the sum, sort the array, and find maximum and minimum.

n = int(input())
ar = list(map(int,input().split()))

print(sum(ar))
ar.sort()
ar.reverse()
print(ar)
print(max(ar),min(ar))
