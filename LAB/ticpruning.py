import random

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def game_over(board):
    return is_winner(board, PLAYER_X) or is_winner(board, PLAYER_O) or is_draw(board)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, PLAYER_X):
        return -1
    if is_winner(board, PLAYER_O):
        return 1
    if is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_O
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER_X
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    alpha = float("-inf")
    beta = float("inf")
    for move in get_available_moves(board):
        board[move[0]][move[1]] = PLAYER_O
        eval = minimax(board, 0, False, alpha, beta)
        board[move[0]][move[1]] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        player_move = None
        while player_move not in get_available_moves(board):
            try:
                row, col = map(int, input("Enter your move (row and column): ").split())
                player_move = (row, col)
                if player_move not in get_available_moves(board):
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        board[player_move[0]][player_move[1]] = PLAYER_X
        print_board(board)

        if not game_over(board):
            computer_move = find_best_move(board)
            board[computer_move[0]][computer_move[1]] = PLAYER_O
            print("Computer's move:")
            print_board(board)

    if is_winner(board, PLAYER_X):
        print("You win!")
    elif is_winner(board, PLAYER_O):
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()



# Welcome to Tic-Tac-Toe!
#   |   |  
# ---------
#   |   |  
# ---------
#   |   |  
# ---------
# Enter your move (row and column): 1 1
#   |   |  
# ---------
#   | X |  
# ---------
#   |   |  
# ---------
# Computer's move:
# O |   |  
# ---------
#   | X |  
# ---------
#   |   |  
# ---------
# Enter your move (row and column): 2 0
# O |   |  
# ---------
#   | X |  
# ---------
# X |   |  
# ---------
# Computer's move:
# O |   | O
# ---------
#   | X |  
# ---------
# X |   |  
# ---------
# Enter your move (row and column): 0 1
# O | X | O
# ---------
#   | X |  
# ---------
# X |   |  
# ---------
# Computer's move:
# O | X | O
# ---------
#   | X |  
# ---------
# X | O |  
# ---------
# Enter your move (row and column): 1 2
# O | X | O
# ---------
#   | X | X
# ---------
# X | O |  
# ---------
# Computer's move:
# O | X | O
# ---------
# O | X | X
# ---------
# X | O |  
# ---------
# Enter your move (row and column): 2 2
# O | X | O
# ---------
# O | X | X
# ---------
# X | O | X
# ---------
# It's a draw!