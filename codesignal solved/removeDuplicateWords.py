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
