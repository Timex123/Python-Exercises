import random


game = [[random.randint(1,2), random.randint(1,2), random.randint(1,2)],
        [random.randint(1,2), random.randint(1,2), random.randint(1,2)],
        [random.randint(1,2), random.randint(1,2), random.randint(1,2)]]
print(game)

#Player 1 wins when:

if game[0][0] == 1 and game[0][0] == game[1][0] == game[2][0]:
        print("Player 1 wins the game")
if game[0][1] == 1 and game[0][1] == game[1][1] == game[2][1]:
        print("Player 1 wins the game")
if game[0][2] == 1 and game[0][2] == game[1][2] == game[2][2]:
        print("Player 1 wins the game")
if game[0][0] == 1 and game[0][0] == game[0][1] == game[0][2]:
        print("Player 1 wins the game")
if game[1][0] == 1 and game[1][0] == game[1][1] == game[1][2]:
        print("Player 1 wins the game")
if game[1][0] == 1 and game[1][0] == game[1][1] == game[1][2]:
        print("Player 1 wins the game")
if game[0][0] == 1 and game[0][0] == game[1][1] == game[2][2]:
        print("Player 1 wins the game")
if game[2][0] == 1 and game[2][0] == game[1][1] == game[2][0]:
        print("Player 1 wins the game")



