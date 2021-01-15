"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
words = ["cat", "bt", "hat", "tree"]
chars = "atach"


def countCharacters(words, chars):
    # for each word in words check if it can be made from the chars only
    # using a specific char once
    result = 0
    for word in words:
        good_word = True
        chars_copy = list(chars)
        for char in word:
            if char not in chars_copy:
                good_word = False
                break
            else:
                chars_copy.remove(char)
        if good_word:
            result += len(word)
    return result

# print(f'countChars: {countCharacters(words, chars)}')
