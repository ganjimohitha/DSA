# Question: Convert a decimal number to base 3.

digits = []

b = 3
n = 9

while (n > 0):
    digits.append(n%b)
    n //= b # integer division and n /= b means it's an floor division

print(digits[::-1])
