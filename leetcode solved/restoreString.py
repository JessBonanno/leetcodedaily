"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.



Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"
Example 5:

Input: s = "art", indices = [1,0,2]
Output: "rat"
"""

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]


def restoreString(s, indices):
    # match the word to the array in a dict
    # return the key for numbers in order from the dict
    # mapped = dict(zip(s, indices))
    mapped = {}
    cur_idx = 0
    result = ''

    for i in range(len(s)):
        if s[i] not in mapped:
            mapped[s[i]] = []
        mapped[s[i]].append(indices[i])

    while cur_idx <= len(indices):
        for key in mapped:
            if cur_idx in mapped[key]:
                result += key
        cur_idx += 1

    return result

# print(f'restoreString(codeleet, [4,5,6,7,0,2,1,3]: {restoreString(s, indices)}')
