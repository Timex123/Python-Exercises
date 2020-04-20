a = [1, 1, 2, 3, 4, 5, 8, 10, 15, 20, 100]
i = 0
while a[i] < 5:
    print(a[i])
    i = i+1
    if a[i] >= 5:
        break

i = 0
list = []

while a[i] < 5:
    list.append(a[i])
    i = i+1
    if a[i] >= 5:
        break
print(list)


