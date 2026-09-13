# Question: Calculate the gross salary.

salary = int(input())

if salary <= 10000:
    hra = salary * 0.20
    da = salary * 0.80
elif salary <= 20000:
    hra = salary * 0.25
    da = salary * 0.90
else:
    hra = salary * 0.30
    da = salary * 0.95

gross = salary + hra + da
print(f"Gross Salary is {gross}")
