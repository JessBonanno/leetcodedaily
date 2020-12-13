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


"""
997. Find the Town Judge
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""

N = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]


def findJudge(N, trust):
    # initialize dict to hold trust relationships
    trusted = {}
    # create an empty trusted array for each person (N) in the trusted dict
    for i in range(1, N + 1):
        trusted[i] = []
    # add the relationships to the dict
    for groups in range(len(trust)):
        if trust[groups][0] not in trusted:
            trusted[trust[groups][0]] = []
        trusted[trust[groups][0]].append(trust[groups][1])
    # initialize the judge to not exist
    judge = -1
    # iterate the trusted relationships
    for person in trusted:
        # if someone trusts nobody
        if trusted[person] == []:
            # set the judge to that person
            judge = person
            # check to see if everyone else trusts that pers
    for person in trusted:
        # if anyone does not trust the judge return -1 there is no judge
        if judge not in trusted[person] and person != judge:
            return -1
    # if we reach the end the judge is valid
    return judge


# print(findJudge(N, trust))


"""
299. Bulls and Cows
Medium

858

997

Add to List

Share
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"
Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"
"""

# bulls are digits in correct place
# cows are correct digits in wrong place

secret = "1122"
guess = "2211"
expected = "0A4B"
secret = "1123"
guess = "0111"
expected = "1A1B"
secret = "9305"
guess = "9205"
expected = "3A0B"


def getHint(secret, guess):
    def getBulls(secret, guess):
        # init new guess and secret
        new_guess = guess
        new_secret = secret
        # init found_bulls
        found_bulls = ''
        for i in range(len(guess)):
            # if guess and secret match at index
            if guess[i] == secret[i]:
                # add the guess to the found bulls
                found_bulls += guess[i]
                # remove the match from the guess and secret
                new_secret = new_secret.replace(secret[i], '', 1)
                new_guess = new_guess.replace(guess[i], '', 1)
        # return the bulls and the new secret and guess
        return found_bulls, new_secret, new_guess

    # helper to find cows
    def getCows(secret, guess):
        # init cows count
        cows = 0
        for i in range(len(guess)):
            # if the guess is in the secret
            if guess[i] in secret:
                # increment the cow count
                cows += 1
                # remove the guessed item from the secret
                secret = secret.replace(guess[i], '', 1)
        # return the found cows
        return cows

    # get the bulls, new secret and guess by calling getBulls helper
    bulls, new_secret, new_guess = getBulls(secret, guess)
    # get the cows by calling getCows with the new secret and guess obtained
    # from get cows
    cows = getCows(new_secret, new_guess)
    # return the length of bulls as bulls and the cows
    return f'{len(bulls)}A{cows}B'


print(getHint(secret, guess))
