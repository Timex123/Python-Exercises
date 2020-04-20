print("Please pick one:"
      "     rock"
      "     paper"
      "     scissors")

while True:
      game = {'rock': 1, 'scissors': 2, 'paper': 3}
      player_a = str(input("Player 1: "))
      player_b = str(input("Player 2: "))
      a = game.get(player_a)
      b = game.get(player_b)
      dif = a-b

      if dif in [-1, 2]:
            print("player 1 wins")
            break
      if dif in [-2, 1]:
            print("player 2 wins")
            break
      else:
            print("Draw")
print("Game over")
