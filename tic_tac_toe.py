import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print("\n")
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---+---+---")
    print()

# Print position numbers
def print_positions():
    print("\nBoard Positions:\n")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9\n")

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True

    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score

# AI Move
def ai_move():

    best_score = -math.inf
    move = -1

    for i in range(9):

        if board[i] == ' ':

            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

# Human Move
def player_move():

    while True:

        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Choose number between 1 and 9")
                continue

            if board[position-1] != ' ':
                print("Position already occupied")
                continue

            board[position-1] = 'X'
            break

        except ValueError:
            print("Invalid input")

# Main Game
def play():

    print("===== TIC TAC TOE AI =====")

    print_positions()

    while True:

        print_board()

        player_move()

        if check_winner('X'):
            print_board()
            print("Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("Game Draw!")
            break

        print("AI is thinking...\n")

        ai_move()

        if check_winner('O'):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("Game Draw!")
            break

play()