"""
Merging Strings
---------------
You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".



You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.

Example

For s1 = "dce" and s2 = "cccbd", the output should be
mergeStrings(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.



For s1 = "super" and s2 = "tower", the output should be
mergeStrings(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length ≤ 104.

[input] string s2

A string consisting only of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length ≤ 104.

[output] string

The string that results by merging s1 and s2 using your special merge function.
"""

s1 = "super"
s2 = "tower"

s1 = "dce"
s2 = "cccbd"

s1 = "kkihj"
s2 = "jbsmfoftph"
expected = "jbsmfoftphkkihj"

s1 = "ougtaleegvrabhugzyx"
s2 = "wvieaqgaegbxg"
output = "owvieaqugaegbxggtaleegvrabhugzyx"
expected = "owvieaqugtaleegvrabhugzyxgaegbxg"


# fully passing
def mergeStrings(s1, s2):
    # variable to hold the result
    result = ''
    # variable to hold the current index of the longer of the two strings
    s2_index = 0
    # variable to hold the current index of the shorter of the two strings
    s1_index = 0
    # variables for the s2 string and the s1 string
    # s2 = ''
    # s1 = ''
    # logic to find the s2 and s1 strings from the given strings
    # if len(s1) > len(s2):
    #     s2 = s1
    #     s1 = s2
    # else:
    #     s2 = s2
    #     s1 = s1
    # hash maps for each string to hold the number of occurrences of each
    # letter
    s1_map = {}
    s2_map = {}
    # logic creating the hash maps
    for letter in s1:
        if letter not in s1_map:
            s1_map[letter] = 0
        s1_map[letter] += 1

    for letter in s2:
        if letter not in s2_map:
            s2_map[letter] = 0
        s2_map[letter] += 1
    # print('s1 map:', s1_map)
    # print('s2 map:', s2_map)
    # while the s1 string current index is less than the s1 string length
    # and the s2 string index is shorter than the s2 string length
    # (keeps us from index out of bounds error)
    while s1_index < len(s1) and s2_index < len(s2):
        # print('s1', s1)
        # print('s2', s2)
        # print('result:', result)
        # print('compare', 's1', s1[s1_index], 's2', s2[s2_index])
        # my print statements for debugging
        # print('i', i)
        # print('s2_index', s2_index)
        # print(chr(max(ord(s1[i]), ord(s2[s2_index]))))
        # if the letter count for the s1 string letter at current s1
        # string index is less than the letter count for the s2 string
        # letter at current s2 string index
        if s1_map[s1[s1_index]] < s2_map[s2[s2_index]]:

            # print('s1 i', s1[i])
            # print('count', s1_map[s1[i]])
            # print('s2 i', s2[s2_index])
            # print('count', s2_map[s2[s2_index]])
            # add the letter from the s1 string at the current index to
            # the result
            result += s1[s1_index]
            # increment the s1 string current index
            s1_index += 1
        # if the letter count for the s1 string letter at the current
        # index is greater than the letter count for the s2 string letter
        # at current s2 string index
        elif s1_map[s1[s1_index]] > s2_map[s2[s2_index]]:
            # add the letter from the s2 string at the current index to the
            # result
            result += s2[s2_index]
            # increment the s2 string current index
            s2_index += 1
        # if both letter have the same number of occurrences in their
        # respective strings
        else:
            if ord(s1[s1_index]) == ord(s2[s2_index]):
                result += s1[s1_index]
                s1_index += 1
            else:
                # add the letter that comes first sequentially
                result += chr(min(ord(s1[s1_index]), ord(s2[s2_index])))
                # if the s2 string letter was added
                if ord(s1[s1_index]) > ord(s2[s2_index]):
                    # increment the s2 string current index
                    s2_index += 1
                # else if the s1 string letter was added
                else:
                    # increment the s1 string current index
                    s1_index += 1
    # if the s1 string index is at the end of the string
    # we have added all the letters in that string and can just add the rest
    # of the letters in the s2 string to the result in the order they are in
    if s1_index == len(s1):
        # add rest of the s2 string from the current index to the end of
        # the string
        result += s2[s2_index:]
    # if the s2 string index is at the end of the string
    # we have added all the letters in that string and can just add the rest
    # of the letters in the s1 string to the result in the order they are in
    if s2_index >= len(s2):
        # add rest of the s1 string from the current index to the end of
        # the string
        result += s1[s1_index:]
    # return the result
    return result


# print('merge strings', mergeStrings(s1, s2))
