game = [[" ", " ", " "],
	    [" ", " ", " "],
	    [" ", " ", " "]]


Dots = " ---"
Line = "|"

i = 0
player_1 = [0, 0]
player_2 = [0, 0]
win = 0

while win != "y":

    while i < 3:
        print(3 * Dots)
        print(Line, game[i][0], Line, game[i][1], Line, game[i][2], Line)
        i = i + 1

    print(3 * Dots)
    i = 0

    print("Player 1 - Input row and column: ")
    insert = input()
    insert.split()
    player_1[0] = int(insert[0])
    player_1[1] = int(insert[2])
    print(player_1)

    game[player_1[0] - 1][player_1[1] - 1] = "X"

    while i < 3:
        print(3 * Dots)
        print(Line, game[i][0], Line, game[i][1], Line, game[i][2], Line)
        i = i + 1

    print(3 * Dots)
    i = 0

    print("Player 2 - Input row and column: ")
    insert = input()
    insert.split()
    player_2[0] = int(insert[0])
    player_2[1] = int(insert[2])
    print(player_2)

    game[player_2[0] - 1][player_2[1] - 1] = "O"
    print(game)

    while i < 3:
        print(3 * Dots)
        print(Line, game[i][0], Line, game[i][1], Line, game[i][2], Line)
        i = i + 1

    print(3 * Dots)
    i = 0
    win = input("Did somebody win?: y/n ")