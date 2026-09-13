# Question: Find maximum and minimum values with their indices.

def maxi_min(arr):
    maxi = arr[0]
    mini = arr[0]
    maxi_idx = 0
    mini_idx = 0
    for i in range(1,len(arr)):
        if arr[i] >= maxi:
            maxi = arr[i]
            maxi_idx = i

        if arr[i] <= mini:
            mini = arr[i]
            mini_idx = i

    return maxi,maxi_idx,mini,mini_idx

ar = list(map(int,input().split()))
a,b,c,d = maxi_min(ar)
print(f"Maximum number is {a} -> at index {b} and Minimum number is {c} -> at index {d}")
