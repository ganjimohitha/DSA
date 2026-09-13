# Question: Print the digits of a number in reverse order.

n = int(input())

while n > 0:
    r = n % 10
    print(r, end=" ")
    n //= 10
