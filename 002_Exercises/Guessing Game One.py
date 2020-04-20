import random


a = random.randint(1, 9)
guess = 0
number = 0

while guess != a and number !="exit":
    number = input("Guess a number: ")
    guess += 1

    if number == "exit" :
        break

    number = int(number)

    if number == a :
        print("You guessed")
        break

    if number < a :
        print("It is too low")

    if number > a :
        print("It is too high")

print(a)
print("You tried ", guess, " times")