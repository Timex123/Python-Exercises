number = int(input("Insert number: "))
i = 1
div = []
while i <= number:
    a = number % i
    if a == 0:
        print(i)
        div.append(i)
    i = i+1
    if len(div) == 3:
        break

if len(div) == 2:
    print(number, "is a prime number")
else:
    print(number, "isn't a prime number")