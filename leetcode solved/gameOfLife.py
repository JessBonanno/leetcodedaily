"""
289. Game of Life
"""
"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies as if caused by 
under-population.
- Any live cell with two or three live neighbors lives on to the next 
generation.
- Any live cell with more than three live neighbors dies, as if by 
over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, 
as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0]
               ,[0,0,1]
               ,[1,1,1]
               ,[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""


def gameOfLife(board):


    # init array of neighbor positions
    neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1),
                 (1, 1)]
    # init length of rows
    rows = len(board)
    # init length of cols
    cols = len(board[0])

    # init copy of board
    copy_board = [[board[row][col] for col in range(cols)] for row in
                  range(rows)]

    # iterate board cell by cell.
    for row in range(rows):
        for col in range(cols):

            # for each cell count number of live neighbors.
            live_neighbors = 0
            for neighbor in neighbors:
                # placeholders for row and column in case the checks are out
                # of bounds we won't throw an error
                # init r to the row + neighbor[0]
                r = (row + neighbor[0])
                # init c to the col + neighbor[1]
                c = (col + neighbor[1])

                # check for neighbors IN BOUNDS ( in the copy )
                # if r is less than the len of the board and r >= 0
                # AND c is less than len of board[0] and c >= 0
                # AND current neighbor is live (1)
                if (r < rows and r >= 0) and (c < cols and c >= 0) and (
                        copy_board[r][c] == 1):
                    # increment live neighbors
                    live_neighbors += 1

            # - 1 Any live cell with fewer than two live neighbors dies as if
            # caused by
            # under-population.

            # - 3 Any live cell with more than three live neighbors dies,
            # as if by
            # over-population.

            # if a live cells live neighbors is less than 2 or greater than 3
            # kill the cell
            if copy_board[row][col] == 1 and (
                    live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = 0

            # - 4 Any dead cell with exactly three live neighbors becomes a
            # live cell,
            # as if by reproduction.

            # if a dead cell has 3 live neighbors it will become live
            if copy_board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 1

# Rule 2 happens by default
# - 2 Any live cell with two or three live neighbors lives on to the next
# generation.



board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

print(f'gameOfLife: {gameOfLife(board)}')
print(board)
