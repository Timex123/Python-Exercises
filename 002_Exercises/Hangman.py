import random
from random import choice

word = open('SOWPODs.txt').read().split()

word = random.choice(word)

print("Welcome to hangman:")
print(len(word)*"_ ")

IncorrectGuess = 0
UsedLettes = []
OldLetter = []
guess = 0

while IncorrectGuess < 6:
    letter = input("Guess letter: ").capitalize()
    UsedLettes.append(letter)
    a = 0
    while a < len(word):
        if word[a] in OldLetter:
            print(word[a], end=" ")
        if word[a] == letter and word[a] not in OldLetter:
                print(word[a], end=" ")
        if word[a] not in letter and word[a] not in OldLetter:
                print("_", end=" ")
        a = a + 1
    print(" ")
    OldLetter.append(letter)

    if letter not in word:
        print("Incorrect")
        IncorrectGuess = IncorrectGuess + 1

    guess = guess + 1
    print("It was your ", guess, " guess")
    print("Used letters: ", UsedLettes)
    print("U have ", 6 - IncorrectGuess, " chances left.")

if IncorrectGuess == 6:
    print("You lost")
    print(word)