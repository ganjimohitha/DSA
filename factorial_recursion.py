# Question: Find factorial using recursion.

def fact(n):
    if n == 0 or n == 1:
        return 1

    ans = n*fact(n-1)
    return ans

num = int(input())
print(fact(num))
