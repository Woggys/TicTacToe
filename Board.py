
# Board base layout
board = [
    {"A1": ".", "A2": ".", "A3": "."},
    {"B1": ".", "B2": ".", "B3": "."},
    {"C1": ".", "C2": ".", "C3": "."}
]


# Called when starting a new game
def start_game(is_player_one, player_one, player_two):
    print("\n")
    print("Welcome to the game of Tic Tac Toe!")
    print("The Horizontal direction is counted by (1,2,3")
    print("The Vertical direction is counted by (A,B,C) \n")
    print("Get three of the same type in a row to win!")
    if is_player_one:
        print("Player: " + player_one.icon + " will start!")
    else:
        print("Player: " + player_two.icon + " will start!")


# Check if someone won
def check_if_win():
    temp = []
    for i in board:
        for j in i.values():
            temp.append(j)

    # Horizontal Win Condition
    if temp[0] != "." and temp[0] == temp[1] and temp[0] == temp[2]:
        return True
    if temp[3] != "." and temp[3] == temp[4] and temp[3] == temp[5]:
        return True
    if temp[6] != "." and temp[6] == temp[7] and temp[6] == temp[8]:
        return True
    # Vertical Win Condition
    if temp[0] != "." and temp[0] == temp[3] and temp[0] == temp[6]:
        return True
    if temp[1] != "." and temp[1] == temp[4] and temp[1] == temp[7]:
        return True
    if temp[2] != "." and temp[2] == temp[5] and temp[2] == temp[8]:
        return True
    # Diagonal Win
    if temp[0] != "." and temp[0] == temp[4] and temp[0] == temp[8]:
        return True
    if temp[2] != "." and temp[2] == temp[4] and temp[2] == temp[6]:
        return True


# Call when the game finishes
def end_game(is_player_one):
    if is_player_one:
        print("Well played Player Two")
    else:
        print("Well played Player One")

    print_board()
    print('\nTo play another round type "Restart"')
    if input() == "Restart":
        board[0] = {"A1": ".", "A2": ".", "A3": "."}
        board[1] = {"B1": ".", "B2": ".", "B3": "."}
        board[2] = {"C1": ".", "C2": ".", "C3": "."}
        return False, False
    else:
        return True, True


# Start a new round.
def new_round(player_obj):
    print(print_board())
    player_input = player_obj.get_input()
    update_board(player_input, player_obj)


# Get input and update the board
def update_board(player_input, player_obj):
    for i in board:
        if player_input in i:
            i[player_input] = player_obj.icon


# Loop through dictionary and print the values
def print_board():
    for i in board:
        temp = []
        for j in i.values():
            temp.append(j)
        print(temp)
