# LAB1 Implement Tic –Tac –Toe Game.
import random
board = [' ' for i in range(9)]


def genBoard():
    print("\n")
    print(20 * "*")
    print("\n")
    print("    |   |")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print("    |   |")
    print("-------------")
    print("    |   |")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print("    |   |")
    print("-------------")
    print("    |   |")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("    |   |")


def playMove(board):
    move = int(input("Enter a position between 1 to 9:"))
    if move not in range(1, 10):
        print("Move outside permitted range!!")
        playMove(board)
    if not isOccupied(board, move - 1):
        board[move - 1] = 'X'
    else:
        print("Sorry the given cell is occupied")
        playMove(board)
    return


def compMove(board):
    move = random.randint(1, 9)  # inclusive of limit 1 and 9
    if not isOccupied(board, move - 1):
        board[move - 1] = 'O'
    else:
        compMove(board)
    return


def checkForWinner(board, alpha):
    if(
        # rows
      (board[0] == alpha and board[1] == alpha and board[2] == alpha) or
      (board[3] == alpha and board[4] == alpha and board[5] == alpha) or
      (board[6] == alpha and board[7] == alpha and board[8] == alpha) or
        # cols
      (board[0] == alpha and board[3] == alpha and board[6] == alpha) or
      (board[1] == alpha and board[4] == alpha and board[7] == alpha) or
      (board[2] == alpha and board[5] == alpha and board[8] == alpha) or
        # diagonals
      (board[0] == alpha and board[4] == alpha and board[8] == alpha) or
      (board[2] == alpha and board[4] == alpha and board[6] == alpha)):
        return True
    else:
        return False


def isOccupied(board, move):
    if board[move] == ' ':
        return False
    else:
        return True


def isFull(board):
    if ' ' not in board:
        return True
    else:
        return False


def main():

    print("Welcome to TIC TAC TOE!\n")
    print("Opponent is O and you are X:\n")
    while not isFull(board):
        genBoard()
        if not checkForWinner(board, 'O'):
            playMove(board)
            if(isFull(board)):
                break
            genBoard()
        else:
            print("Player O won!")
            quit()
        if not checkForWinner(board, 'X'):
            compMove(board)
            if(isFull(board)):
                break
            genBoard()
        else:
            print("Player X won!")
            quit()

    if (isFull(board)):
        print("The game is a Tie")


main()
