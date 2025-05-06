def is_safe(board, row, col, n):
    # Check this column on upper rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(["".join("Q" if col == 1 else "." for col in r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    print(f"Total solutions for {n}-Queens: {len(solutions)}")
    for sol in solutions:
        for row in sol:
            print(row)
        print()


# Example: Solve 4-Queens
n_queens(4)
