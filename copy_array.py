# Question: Copy an array into another array.

def cntfreq(ar):
    mp = {}
    for i in ar:
        mp[i] = mp.get(i,0)+1

    return mp

n = int(input())
arr = list(map(int,input().split()))
mp = cntfreq(arr)

for a,b in mp.items():
    print(f"{a} --> {b}")
