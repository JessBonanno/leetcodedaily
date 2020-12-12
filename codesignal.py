"""
Codesignal
"""

"""
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
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.
Examples:
`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
[execution time limit] 4 seconds (py3)
[input] string input_str
[output] string
"""

input_str = "my dog is my dog is super smart"


def csRemoveDuplicateWords(input_str):
    word_list = input_str.split()
    words_minus_dups = []
    for word in word_list:
        if word not in words_minus_dups:
            words_minus_dups.append(word)
    return " ".join(words_minus_dups)

# print(csRemoveDuplicateWords(input_str))
