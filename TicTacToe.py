import Player
import Board


game_over = False
first_round = True

is_player_one = True
stop_playing = False

player_one = Player.player("X")
player_two = Player.player("O")

player_one.icon = input(print("Player one. What icon will you use?\n Answer: "))
player_two.icon = input(print("Player Two. What icon will you use?\n Answer: "))
while not stop_playing:

    Board.start_game(is_player_one, player_one, player_two)

    while not game_over:

        if is_player_one:
            Board.new_round(player_one)
            is_player_one = False
        else:
            Board.new_round(player_two)
            is_player_one = True

        game_over = Board.check_if_win()

    game_over, stop_playing = Board.end_game(is_player_one)
