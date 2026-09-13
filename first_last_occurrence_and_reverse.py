# Question: Find first and last occurrence of an element and reverse the array.

def find(ar,x):
    fidx = -1
    lidx = -1
    for i in range(len(ar)):
        if ar[i] == x:
            if fidx == -1:
                fidx = i
                
            lidx = i

    return fidx,lidx

def rev(ar):
    for i in range(len(ar)//2):
        ar[i],ar[len(ar)-1-i] = ar[len(ar)-1-i],ar[i]

    return ar
    
ar = list(map(int,input().split()))
x = int(input())
a,b = find(ar,x)
print(f"{a} -- first and {b} -- last")
print(rev(ar))
