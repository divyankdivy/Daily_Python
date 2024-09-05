import random

print("Welcome to Tic Tac Toe Game")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

winner = None
player_one = "X"
player_two = "O"


def display_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} ")


def submit_move(board_name,comp=False):
    if board_name.count(" ") == 2:
        player_1(board_name)
    else:
        player_1(board_name)
        check_winner(board_name)
        if comp:
            player_2_comp(board_name)
        else:
            player_2(board_name)
    display_board()


def player_1(board_name):
    choice = int(input("Player 1: Please chose a position between 1 to 9: "))
    while 1 <= choice <= 9 and board_name[choice] != " ":
        print("Position is already taken, Chose again")
        choice = int(input("Enter a number between 1 to 9: "))
    board_name[choice] = player_one


def player_2_comp(board_name):
    position = random.randint(1, 9)
    while board_name[position] != " ":
        position = random.randint(1, 9)
    board_name[position] = player_two


def player_2(board_name):
    choice = int(input("PPlayer 2: Please choose a position between 1 to 9: "))
    while 1 <= choice <= 9 and board_name[choice] != " ":
        print("Position is already taken, Chose again")
        choice = int(input("Enter a number between 1 to 9: "))
    board_name[choice] = player_two


def check_winner(board_name):
    if check_row(board_name) or check_col(board_name) or check_diagonal(board_name):
        print(f"Player {winner} won")
        return True
    elif check_tie(board_name):
        print("Its a Tie")
        return False


def check_row(board_name):
    global winner
    if (board_name[1] == board_name[2] == board_name[3]) and board_name[1] != " ":
        winner = board_name[1]
        return True
    elif (board_name[4] == board_name[5] == board_name[6]) and board_name[4] != " ":
        winner = board_name[4]
        return True
    elif (board_name[7] == board_name[8] == board_name[9]) and board_name[7] != " ":
        winner = board_name[7]
        return True
    else:
        return False


def check_col(board_name):
    global winner
    if (board_name[1] == board_name[4] == board_name[7]) and board_name[1] != " ":
        winner = board_name[1]
        return True
    elif (board_name[2] == board_name[5] == board_name[8]) and board_name[2] != " ":
        winner = board_name[2]
        return True
    elif (board_name[3] == board_name[6] == board_name[9]) and board_name[3] != " ":
        winner = board_name[3]
        return True
    else:
        return False


def check_diagonal(board_name):
    global winner
    if (board_name[1] == board_name[5] == board_name[9]) and board_name[1] != " ":
        winner = board_name[1]
        return True
    elif (board_name[3] == board_name[5] == board_name[7]) and board_name[3] != " ":
        winner = board_name[3]
        return True
    else:
        return False


def check_tie(board_name):
    if board_name.count(" ") == 1:
        return True
