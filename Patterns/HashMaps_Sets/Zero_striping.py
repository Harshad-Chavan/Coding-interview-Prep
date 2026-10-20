# Problem statement
#
# You are given an m × n integer matrix.
# If any element in the matrix is 0, set its entire row and entire column to 0.
#
# You must do this in place, meaning you should modify the original matrix rather
# than create a separate matrix for the final result
#
from pprint import pprint

m = 3
n = 3
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

def main():

    # first pass create two hash sets
    zero_rows = set()
    zero_cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)


    # pass two  : check if the cell has an indec in zero_row, zero_col set
    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    for row in matrix:
        print(row)

if __name__ =="__main__":
    main()
