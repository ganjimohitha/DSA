# Question: Find the frequency of every array element.

def cntfreq(ar,key):
    cnt = 0
    for i in ar:
        if i == key:
            cnt += 1

    return cnt

n = int(input())
arr = list(map(int,input().split()))
x = int(input("key : "))
print(cntfreq(arr,x))
