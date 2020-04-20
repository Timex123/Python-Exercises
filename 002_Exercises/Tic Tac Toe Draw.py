game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

player_1 = [0, 0]
player_2 = [0, 0]
insert = 0

i = 0
win = 0

while i <= 5 and win != "y":
	print("Player 1 - Input row and column: ")
	insert = input()
	insert.split()
	player_1[0] = int(insert[0])
	player_1[1] = int(insert[2])
	print(player_1)

	game[player_1[0] - 1][player_1[1] - 1] = "X"
	print(game)

	print("Player 2 - Input row and column: ")
	insert = input()
	insert.split()
	player_2[0] = int(insert[0])
	player_2[1] = int(insert[2])
	print(player_2)

	game[player_2[0] - 1][player_2[1] - 1] = "O"
	print(game)

	win = input("Did somebody win?: y/n ")
	i = i+1