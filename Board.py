import Player

board = [
    {"A1": ".", "A2": ".", "A3": "."},
    {"B1": ".", "B2": ".", "B3": "."},
    {"C1": ".", "C2": ".", "C3": "."}
]


def start_game():
    print("\n")
    print("Welcome to the game of Tic Tac Toe!")
    print("The Horizontal direction is counted by (1,2,3")
    print("The Vertical direction is counted by (A,B,C) \n")
    print("Get three of the same type in a row to win!")


def end_game():
    pass


def new_round():
    print(print_board())
    player_input = Player.get_input()
    update_board(player_input)


def update_board(player_input):
    for i in board:
        if player_input in i:
            pass
            i[player_input] = "X"




def print_board():
    for i in board:
        temp = []
        for j in i.values():
            temp.append(j)
        print(temp)
