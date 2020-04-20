import random

number = random.randint(1000, 9999)
print(number)
number = list(str(number))

print(number)

guess = 0
i = 0
cow = 0
bull = 0
cont = "y"
value = 0

while cont == "y" and value != number:
    value = int(input("Input your number: "))
    value = list(str(value))
    while i < 4:
        x = 0
        if number[i] == value[i]:
            cow = cow + 1
        else:
            while x < 4:
                if number[i] == value[x]:
                    bull = bull + 1
                    x = 4
                x = x + 1
        i = i + 1
    guess = guess + 1

    print(number)
    print(value)
    print("Cows: ", cow, " & Bulls: ", bull)
    cont = input("Do you wish to continue? y/n ")

if value == number:
    print("You needed", guess, "guess to guess")
else:
    print("You tried ", guess, " time(s) and you haven't guessed")