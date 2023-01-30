# Sudoku Solver App


# main solving function
def sudokuSolver(board):
    pos = getEmpty(board)
    if pos == None:
        return True
    else:
        row, col = pos
        for i in range(1, 10):
            if isNumValid(board, row, col, i):
                board[row][col] = i

                if sudokuSolver(board):
                    return True
                board[row][col] = 0
        return False


# Checks if the square is empty and fill a set with the empty squares
def getEmpty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return (r, c)


# Checks if the position is valid to insert the number
def isNumValid(board, row, col, n, x=0):
    # Check row
    for i in range(len(board)):
        if board[row][i] == n and col != i:
            return False

    # Check col
    for i in range(len(board)):
        if board[i][col] == n and row != i:
            return False

    """
    To check the box we'll treat each box as an individual cell of a 3x3 matrix
    To achieve that, all we have to do is divide the row and column position by 3. 
    After that, we multiply by 3 to get the starting range 
    and mult and add 3 to get the end of the range. EZ
    """
    # Check boxes
    boxRow = row // 3
    boxCol = col // 3

    for r in range(boxRow * 3, boxRow * 3 + 3):
        for c in range(boxCol * 3, boxCol * 3 + 3):
            if board[r][c] == n and (r, c) != (row, col):
                return False

    return True


def printBoard(board):
    for i in range(len(board)):
        print(board[i])


board = [
    [9, 0, 1, 0, 0, 5, 4, 8, 0],
    [0, 0, 0, 2, 0, 0, 0, 7, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 6, 0, 0, 9, 1, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 9],
    [6, 0, 8, 0, 7, 0, 0, 4, 0],
    [0, 5, 0, 0, 0, 0, 8, 0, 0],
    [0, 3, 0, 0, 0, 6, 0, 0, 0],
]

printBoard(board)
sudokuSolver(board)
print("-----------------")
printBoard(board)
"""
def fillEmpty(board, eSet):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                eSet.add((r, c))

empty = set()
fillEmpty(board, empty)
"""
