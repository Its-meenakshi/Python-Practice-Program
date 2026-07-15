def print_board(board, N):
    for row in board:
        print(row)
    print()


def is_safe(board, row, col, N):
    # Check the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, N):
    # Base case: All queens are placed
    if row == N:
        print("Solution Found:")
        print_board(board, N)
        return True

    # Try placing queen in every column
    for col in range(N):
        print(f"Trying to place Queen at Row {row}, Column {col}")

        if is_safe(board, row, col, N):
            print(f"Safe → Placing Queen at ({row}, {col})")
            board[row][col] = 1
            print_board(board, N)

            # Recur for next row
            if solve(board, row + 1, N):
                return True

            # Backtrack
            print(f"Backtracking from ({row}, {col})")
            board[row][col] = 0
            print_board(board, N)

        else:
            print(f"Not Safe ({row}, {col})")

    return False


def n_queen(N):
    board = [[0] * N for _ in range(N)]

    if not solve(board, 0, N):
        print("No Solution Exists")


# Driver Code
n_queen(4)