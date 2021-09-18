import random
import Player
import Board


game_over = False

Board.start_game()

while not game_over:

    Board.new_round()

Board.end_game()
