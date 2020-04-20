a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
i = 0
print(len(a))
while i < len(a):
    if a[i] in b:
        if not a[i] in c:
            c.append(a[i])
    i = i+1
    if i > len(a):
        break

print(c)




