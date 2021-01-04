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


"""
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
Example
For n = 240, the output should be
lateRide(n) = 4.
Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
For n = 808, the output should be
lateRide(n) = 14.
808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
The duration of your ride, in minutes. It is guaranteed that you've been riding for less than a day (24 hours).
Guaranteed constraints:
0 ≤ n < 60 · 24.
[output] integer
The sum of the digits the digital timer would show.
"""

n = 808


def lateRide(n):
    # init result
    result = 0
    # init hour equal to n // 60 in string format
    hour = str(n // 60)
    # for every digit in hour
    for digit in hour:
        # convert it back to an int and add it to the result
        result += int(digit)
    # init mins equal to ( n - hour in int format * 60 ) in string format
    mins = str(n - (int(hour) * 60))
    # for every digit in mins
    for digit in mins:
        # convert it back to an int and add it to the result
        result += int(digit)
    return result


print(f'lateRide(n): {lateRide(n)}')

"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
Example
For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
Guaranteed constraints:
1 ≤ n < 104.
[output] integer
The area of the n-interesting polygon.
"""

n = 3


def shapeArea(n):
    # the area is equal to n squared + (n - 1) squared
    return n ** 2 + (n - 1) ** 2


print(f'shapeArea(n): {shapeArea(n)}')

"""
Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.
Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.
Example
For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99.
Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer nums
Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-105 ≤ nums[i] ≤ 105.
[input] integer k
Guaranteed constraints:
1 ≤ k ≤ nums.length.
"""

nums = [7, 6, 5, 4, 3, 2, 1]
k = 2


def kthLargestElement(nums, k):
    # sort the array in descending order
    sorted_nums = sorted(nums, reverse=True)
    # iterate the sorted array
    for i in range(len(sorted_nums)):
        # when we reach k - 1 we have our result because of zero based index
        if i == k - 1:
            return sorted_nums[i]


print(
    f'kthLargestElement(nums, k): {kthLargestElement(nums, k)}')




"""
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
Here is some info on Unix file system paths:
/ is the root directory; the path should always start with it even if it isn't there in the given path;
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
this also means that // stands for "change the current directory to the current directory"
. is used to mark the current directory;
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.
Example
For path = "/home/a/./x/../b//c/", the output should be
simplifyPath(path) = "/home/a/b/c".
Here is how this path was simplified:
* /./ means "move to the current directory" and can be replaced with a single /;
* /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
* // means "move to the current directory" and can be replaced with a single /.
Input/Output
[execution time limit] 4 seconds (py3)
[input] string path
A line containing a path presented in Unix style format. All directories in the path are guaranteed to consist only of English letters.
Guaranteed constraints:
1 ≤ path.length ≤ 5 · 104.
"""

path = "/home/a/./x/../b//c/"


def simplifyPath(path):
    # EDGE CASE if path is '/' just return it
    if path == "/":
        return path
    # standardizing all paths to end with '/'
    if path[len(path) - 1] != "/":
        path += "/"
    # standardizing all paths to start with '/'
    if path[0] != "/":
        path = "/" + path
    # init cur path to hold path we are processing
    cur_path = ""
    # init array to hold each path
    path_arr = []
    # iterate the length of the path
    for i in range(1, len(path)):
        # if the current character is not '/'
        if path[i] != "/":
            # add the current character to the current path
            cur_path += path[i]
        #  at this point we have the entire current path
        else:
            # if the current path is a directory ( not '.' or '..' or empty string)
            if cur_path != ".." and cur_path != "." and cur_path != "":
                # add the current path to the list of paths
                path_arr.append(cur_path)
                # reset the current path
                cur_path = ""
            # if the current path is '..' pop off the top of the stack as long
            # the stack is not empty
            elif cur_path == ".." and len(path_arr) != 0:
                path_arr.pop()
                # reset the current path
                cur_path = ""
            cur_path = ""
    # initialize an empty string to hold our result
    result = "/"
    # iterate the list of paths
    for i in range(len(path_arr)):
        # if we are not at the last path in the list
        if i != len(path_arr) - 1:
            # add the path followed by '/' to the result
            result += path_arr[i] + "/"
        # if we are at the last path
        else:
            # only add the path without the trailing '/'
            result += path_arr[i]
    # return the result
    return result


print(f'simplifyPath(path = "/home/a/./x/../b//c/"): {simplifyPath(path)}')


def maxDepth(s):
    # init results and current equal to 0
    res = 0
    cur = 0
    # iterate chars in s
    for char in s:
        # if char is opening paren
        if char == '(':
            # add 1 to current streak of nested parens
            cur += 1
            # set result equal to whatever is more between the current result
            # or current streak
            res = max(res, cur)
        # each time we hit closing paren we close the streak of nested parens
        # by 1
        if char == ')':
            cur -= 1
    # return the result
    return res


s = "(1+2)/(5+((4-9+8)*((1+8+(5*7)*4)/(7+9-5)))/(7/3-8-4-8))"

print(f'maxDepth(s), {maxDepth(s)}')

