import random

guess = 0
number = random.randint(0, 100)
a = 0
b = 0
number_tab = [number]
lower = 0
higher = 100

while a != "y":
    print(number)
    print("Is that your number?: y/n")
    a = input()
    if a == "n":
        print("Is that lower or higher number?: l/h")
        b = input()
    if b == "l":
        lower = number
        number = random.randint(number_tab[guess]+1, higher)
    if b == "h":
        higher = number
        number = random.randint(lower, number_tab[guess]-1)
    number_tab.append(number)
    guess += 1
print("You guessed ", guess, " times")