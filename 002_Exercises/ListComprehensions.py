a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0

b = []
c = []
while i < len(a):
    if a[i]%2 == 0:
        b.append(a[i])
    i = i + 1
    if i == len(a):
        break
print(b)
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]
print(ages)

for z in a:
    if z%2 == 0:
        c.append(z)
print(c)

d = [x for x in a if x%2 == 0]
print(d)