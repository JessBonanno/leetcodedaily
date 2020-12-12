"""
Daily Leetcode practice
"""

"""
164. Maximum Gap 
Hard
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""

nums = [3, 6, 9, 1]


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    ordered = sorted(nums)
    largestDiff = 0
    for i in range(len(ordered) - 1):
        diff = ordered[i + 1] - ordered[i]
        if diff > largestDiff:
            largestDiff = diff
    return largestDiff


# print(maximumGap(nums))


"""
1304. Find N Unique Integers Sum up to Zero
Easy

426

255

Add to List

Share
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
"""

n = 5
import random


def sumZero(n):
    # Initial try less efficient
    # result = []
    # sum = 0
    # for i in range(n - 1):
    #     num = random.randint(0, n * 10)
    #     while num in result:
    #         num = random.randint(0, n * 10)
    #     result.append(num)
    #     sum += num
    #
    # result.append(-sum)
    # return result

    # much more efficient by cutting the loop in 1/2
    count = 1000
    res = []
    i = n
    while i >= 2:
        i -= 2
        res.append(count)
        res.append(count * -1)
        count -= 1

    if i == 1:
        res.append(0)
    return res


# print(sumZero(n))

"""
Rando Codesignal challenge 
find the number if digit anagrams in an array
"""
arr = [25, 35, 872, 228, 53, 278, 872]


def numAnagrams(arr):
    # iterate the length of the array
    # create a sorted set out of the string version of the current integer
    # if that is not already in the results array
    # append it to the array
    # return the length of the results array
    seen = []
    for i in range(len(arr)):
        int_to_set = sorted(list(str(arr[i])))
        if int_to_set not in seen:
            seen.append(int_to_set)
    return len(seen)


# create a results array to hold combinations already seen


# print(numAnagrams(arr))


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

print(alphabetBoardPath(target))
