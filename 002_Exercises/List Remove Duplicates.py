a = [1, 1, 2, 3, 4, 4, 2, 3, "a", "a", "b", 1.23, 1.23, 1.45]

print(a)

def Remove_Duplicates(a):
    i = 0
    z = 0
    x = 0
    b = []
    while i < len(a):
        while z < len(a):
            while x <= len(b):
                if a[i] == a[z]:
                    if a[i] not in b:
                        b.append(a[i])
                        print(b)
                x = x+1
            x = 0
            z = z+1
        z = 0
        i = i+1

    return b

print("After removal: ", Remove_Duplicates(a))