"""
Are Following Patterns
----------------------
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string strings

An array of strings, each containing only lowercase English letters.

Guaranteed constraints:
1 ≤ strings.length ≤ 105,
1 ≤ strings[i].length ≤ 10.

[input] array.string patterns

An array of pattern strings, each containing only lowercase English letters.

Guaranteed constraints:
patterns.length = strings.length,
1 ≤ patterns[i].length ≤ 10.

[output] boolean

Return true if strings follows patterns and false otherwise.
"""

strings = ["cat",
           "dog",
           "dog"]
patterns = ["a", "b", "c"]


def areFollowingPatterns(strings, patterns):
    # check if strings and patterns lengths are the same if not just return
    # False
    if len(strings) != len(patterns):
        return False
    # create a map to hold pattern item as key and string item as value
    pattern_map = {}

    # iterate through the patterns
    for i in range(len(patterns)):
        # if the current patter in not in the dict add it
        if patterns[i] not in pattern_map:
            # if string item in not already a value in the              dict
            if strings[i] not in pattern_map.values():
                pattern_map[patterns[i]] = strings[i]
            else:
                # set pattern item to empty string because   s   string item does
                # not correspond
                pattern_map[patterns[i]] = ''
                return False
        # if the value set to the pattern item does not equal the current
        # string item
        elif pattern_map[patterns[i]] != strings[i]:
            return False

    print(pattern_map)
    return True


print(areFollowingPatterns(strings, patterns))
