print("Gib mir die Nummer:")
a = int(input("Die Nummer ist:"))
b = []
i = 1
while i < a:
    if a%i == 0:
        b.append(i)
        i = i+1
    else:
        i = i+1

for elem in b:
    print(elem)


