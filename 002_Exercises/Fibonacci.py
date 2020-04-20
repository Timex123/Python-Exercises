def Fib():
    num = int(input("How many numbers to generate?: "))
    i = 1
    if num == 0:
        fib = []
    if num == 1:
        fib = [1]
    if num == 2:
        fib = [1, 1]
    if num > 2:
        fib = [1, 1]
        while i < (num-1) :
            fib.append(fib[i]+fib[i-1])
            i = i+1
    return fib

print(Fib())