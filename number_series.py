# Question: Generate the number series.

"""a = 0
b = 1
print(a,b,end = " ")
n = 3
while(n <= 20):
    c = a+b*2
    print(c,end = " ")
    a,b = b,c
    n += 1"""



a, b = 0, 1

for i in range(20):
    print(a, end=" ")
    a, b = b, a + 2 * b
