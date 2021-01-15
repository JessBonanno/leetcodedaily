"""
1138. Alphabet Board Path
Medium

301

86

Add to List

Share
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.



Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
"""

target = 'gzz'
Output = "DR!DDDLD!!"
# target = 'zdz'
# output = "DDDDD!UUUUURRR!DDDDLLLD!"
target = 'zsz'
output = "DDDDD!UURRR!DLLLD!UUUR!"

board = [["a", "b", "c", "d", "e"],
         ["f", "g", "h", "i", "j"],
         ["k", "l", "m", "n", "o"],
         ["p", "q", "r", "s", "t"],
         ["u", "v", "w", "x", "y"],
         ["z"]]


def alphabetBoardPath(target):
    # initialize result string to hold result
    result = ""
    # initialize holders for current row / col
    cur_row = 0
    cur_col = 0
    # initialize holders for target row / col
    target_row = 0
    target_col = 0

    # helper functions
    def get_h_moves(target_col, cur_col):
        # decide if we need to move left (target less than current)
        # or right (target greater than current)
        if target_col > cur_col:
            # get the difference
            h_moves = target_col - cur_col
            print(f'move right {h_moves} times')
            return "R" * h_moves
        else:
            h_moves = cur_col - target_col
            print(f'move left {h_moves} times')
            return "L" * h_moves

    # def get_v_moves:
    #     pass
    # for each letter in target
    for char in target:
        print(f"start: col: {cur_col}, row: {cur_row}")
        # if char exists at current position add ! to result
        if board[cur_row][cur_col] == char:
            result += "!"
        else:
            # else check board to see where it exists from [0,0] using UDRL
            # first find the row where it exists
            for i in range(len(board)):
                if char in board[i]:
                    target_row = i
            # next find the column
            for i in range(len(board[target_row])):
                if board[target_row][i] == char:
                    target_col = i
            # if the target letter is in the current row
            if target_row == cur_row:
                result += get_h_moves(target_col, cur_col)
                result += "!"
                cur_col = target_col

            elif target_row > cur_row:
                v_moves = target_row - cur_row
                print(f'move down {v_moves} times')
                # handle if col we need to move down to z
                print('len', len(board))
                print('cur', cur_row)
                if target_row == 5:
                    print('test')
                    print('v test', v_moves)
                    if cur_row == 0:
                        result += "D" * 4
                    else:
                        result += "D" * (v_moves - 1)
                    cur_row = target_row - 1
                    result += get_h_moves(target_col, cur_col)
                    cur_col = target_col
                    result += "D"
                    cur_row = target_row
                    result += "!"
                else:

                    result += "D" * v_moves
                    cur_row = target_row
                    result += get_h_moves(target_col, cur_col)
                    cur_col = target_col
                    result += "!"



            else:
                v_moves = cur_row - target_row
                print(f'move up {v_moves} times')
                result += "U" * v_moves
                cur_row = target_row
                result += get_h_moves(target_col, cur_col)
                cur_col = target_col
                result += "!"

    return result

# need to update cur values when we find the target letter

# print(alphabetBoardPath(target))
