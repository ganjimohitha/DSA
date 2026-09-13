# Question: Find the sum of i divided by i factorial.

def swap(arr):
    for i in range(0,len(arr)-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
        
def leftswap(ar,k):
    while k > 0:
        temp = ar[0]
        for i in range(len(ar)-1):
            ar[i] = ar[i+1]
        ar[len(ar)-1] = temp
        k -= 1
    
ar = list(map(int,input().split()))
k = int(input())
leftswap(ar,k)
print(ar)
