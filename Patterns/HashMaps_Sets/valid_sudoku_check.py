# Problem: Determine whether a 9 × 9 Sudoku board is valid.
#
# You are given a 2D list representing a Sudoku board. Check whether the board is valid according to the following rules.
# Rules
# 1. Each row must not contain duplicate digits from 1 to 9.
# 2. Each column must not contain duplicate digits from 1 to 9.
# 3. Each of the nine 3 × 3 sub-boxes must not contain duplicate digits from 1 to 9.
# 4. Empty cells are represented by "." and should be ignored.
# Important: You only need to validate the current board. You do not need to solve the Sudoku.


valid_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

def verify_sudoku(board):
    # create a hash set for each row
    row_hsets = [set() for _ in range(9)]
    col_hsets = [set() for _ in range(9)]

    subgrid = [[ set() for _ in range(3)] for _ in range(3)]

    for i in range(9): # for row
        for j in range(9): # for col

            check_num = board[i][j]
            if check_num == ".":
                continue

            # check in row
            if check_num in row_hsets[i]:
                return False

            # check in col
            if check_num in col_hsets[j]:
                return False

            # check in subggrid
            if check_num in subgrid[i //3][j //3]:
                return False

            row_hsets[i].add(check_num)
            col_hsets[j].add(check_num)
            # add in the grid
            subgrid[i //3][j //3].add(check_num)

    return True




if __name__ == "__main__":
    print(verify_sudoku(valid_board))