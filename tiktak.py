def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column should be between 1 and 3.")
            continue

        if board[row][col] != " ":
            print("That position is already taken. Choose another position.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board):
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
