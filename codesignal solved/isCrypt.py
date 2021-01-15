
"""
*** is crypt solution ***
-------------------------
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
"""

crypt = ["SEND", "MORE", "MONEY"]

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]


# my solution
def isCryptSolution(crypt, solution):
    # for each string get the numbers for each character
    num_arr = []
    nums = ''
    for word in crypt:
        for char in word:
            for sect in solution:
                if char in sect:
                    nums += sect[1]
        if len(nums) > 1 and nums.startswith('0'):
            return False
        num_arr.append(nums)
        nums = ''
    pointer = 0
    total = 0
    while pointer < len(num_arr) - 1:
        total += int(num_arr[pointer])
        pointer += 1
    if total != int(num_arr[len(num_arr) - 1]):
        return False
    return True


# most voted code signal solution
# def isCryptSolution(crypt, solution):
#     dic = {ord(c): d for c, d in solution}
#     *v, = map(lambda x: x.translate(dic), crypt)
#     return not any(x != "0" and x.startswith("0") for x in v) and \
#         int(v[0]) + int(v[1]) == int(v[2])


# print(isCryptSolution(crypt, solution))
