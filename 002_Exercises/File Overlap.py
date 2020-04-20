a = open('Prime Numbers.txt', 'r')
Prime = [line.strip() for line in a]
b = open('Happy Numbers.txt', 'r')
Happy = [line.strip() for line in b]

Overlap = []
i = 0
x = 0

while i < len(Prime):
    while x < len(Happy):
        if Happy[x] == Prime[i]:
            Overlap.append(Happy[x])
        x = x + 1
    i = i + 1
    x = 0

print(Overlap)
