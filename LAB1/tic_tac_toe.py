# game logic
# *****************************
# board
# play game
# current player
# check winner:
#   1.check_column
#   2.check_row
#   3.check_diagonal
# check tie
# switching player
# 3x3 board
# generating a board
import random
import sys
global count

global active_player


active_player = "X"  # by default assuming X


def new_board():

    for index, i in enumerate(board):
        count = index + 1

        if count % 3 == 0:
            print(i, end="\n")

        else:
            print(i, end=" | ")

    print(20 * "-")

# starting fresh game


def new_game():
    global board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    continue_game = True
    new_board()
    print("WELCOME TO TIC TAC TOE:\n")
    print("Starting with X")
    c = 1
    while continue_game:

        active_player = "X" if c == 1 else switch_player(active_player)
        player_move(active_player)
        outcome = game_outcome()
        if outcome == True:
            print("We have a Winner:")
            print(active_player)

            board.clear()

            if input("Do you want to play again:y/n?").lower() == 'y':
                new_game()
            else:
                sys.exit()
        elif outcome == "Draw":
            print("Draw")
            board.clear()

            if input("Do you want to play again:y/n?").lower() == 'y':
                new_game()
            else:
                sys.exit()

        else:
            c += 1
            continue

        # game_outcome()

# toggling player


def switch_player(current):
    switched_player = "O" if current == "X" else "X"
    return switched_player

# checking if cell is occupied


def comp_move():  # assuming computer always plays X
    available_list = [index for index, i in enumerate(board) if i == '-']
    comp_choice = random.choice(available_list)
    return comp_choice + 1


def check_if_occupied(userchoice):
    for index, i in enumerate(board):
        if (userchoice - 1 == index):
            if (i == 'X' or i == 'O'):
                return True
            else:
                return False
    return False


def player_move(current):
    global user_choice
    global valid_move
# int(input("Player {} please enter a free position between 1 to 9:".format(
#         current)))
    user_choice = comp_move() if current == "X" else int(
        input("Player {} please enter a free position between 1 to 9:".format(current)))

    if user_choice not in [(i + 1) for i in range(9)]:
        print(user_choice)
        print("Enter a VALID Position:")
        player_move(current)
    else:
        valid_move = check_if_occupied(user_choice)

    # print(valid_move)
    if not valid_move:
        if current == "X":
            board[user_choice - 1] = "X"
            new_board()
        else:
            board[user_choice - 1] = "O"
            new_board()
    else:
        print(valid_move)
        print("Not a valid move. Its already occupied. Try again")
        player_move(current)


def game_outcome():
    # if any check returns True then its false
    if (check_row() or check_col() or check_diag()):
        return True
    elif (all_filled()):
        return "Draw"
    else:
        return False


def all_filled():
    for i in board:
        if i == "-":
            return False
    return True


'''row check'''


def check_row():
    global c1, c2
    c1 = 0
    c2 = 3
    global row
    row = []
    while(c1 != 9):

        for i in range(c1, c2):

            row.append(board[i])

        if(row == ["X", "X", "X"] or row == ["O", "O", "O"]):
            return True
        else:
            row.clear()
            c1 = c2
            c2 += 3
    return False


'''row check'''


def check_col():
    global c1, c2
    c1 = 0
    c2 = 6
    global col
    col = []
    while c2 != 9:

        for i in range(c1, c2 + 1, 3):

            col.append(board[i])

        if(col == ["X", "X", "X"] or col == ["O", "O", "O"]):
            return True
        else:
            col.clear()
            c1 += 1
            c2 += 1

    return False


'''diagonal check'''


def check_diag():
    global c1, c2
    c1 = 0
    c2 = 9
    global diag, diag1
    diag = []
    diag1 = []
    for i in range(c1, c2, 4):  # leading diagonal

        diag.append(board[i])

        if(diag == ["X", "X", "X"] or diag == ["O", "O", "O"]):
            return True
    c1 = 2
    c2 = 7
    for i in range(c1, c2, 2):  # other diagoanal

        diag1.append(board[i])

        if(diag1 == ["X", "X", "X"] or diag1 == ["O", "O", "O"]):
            return True
    return False


new_game()
