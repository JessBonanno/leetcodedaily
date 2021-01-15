"""
Concatenations Sum
------------------
Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

Example

For a = [10, 2], the output should be concatenationsSum(a) = 1344.

a[0] ∘ a[0] = 10 ∘ 10 = 1010,
a[0] ∘ a[1] = 10 ∘ 2 = 102,
a[1] ∘ a[0] = 2 ∘ 10 = 210,
a[1] ∘ a[1] = 2 ∘ 2 = 22.
So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

For a = [8], the output should be concatenationsSum(a) = 88.

There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

a[0] ∘ a[0] = 1 ∘ 1 = 11,
a[0] ∘ a[1] = 1 ∘ 2 = 12,
a[0] ∘ a[2] = 1 ∘ 3 = 13,
a[1] ∘ a[0] = 2 ∘ 1 = 21,
a[1] ∘ a[1] = 2 ∘ 2 = 22,
a[1] ∘ a[2] = 2 ∘ 3 = 23,
a[2] ∘ a[0] = 3 ∘ 1 = 31,
a[2] ∘ a[1] = 3 ∘ 2 = 32,
a[2] ∘ a[2] = 3 ∘ 3 = 33.
The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.
"""

a = [8]

a = [1, 2, 3]


# a = [0, 0]


# needs to be optimized to pass all tests currently 250/300
# def concatenationsSum(a):
#     # variable for the result of the integer addition of concatenated strings
#     result = 0
#     # variables for the current index and the index of the number being added
#     front_index = 0
#     back_index = 0
#     # iterate the array
#     while front_index < len(a):
#         # if the number being added is the last one
#         if back_index == len(a) - 1:
#             # do the concatenation
#             result += int(str(a[front_index]) + str(a[back_index]))
#             # increment the current index
#             front_index += 1
#             # reset the sum index to 0
#             back_index = 0
#         # otherwise just do the concatenation and increase the index of
#         # number being added
#         else:
#             result += int(str(a[front_index]) + str(a[back_index]))
#             back_index += 1
#
#     # return the result
#     return result
def concatenationsSum(a):
    # UPER
    # Understand:
    # we're going to need to return an int after concatenating strings --> int(str() ...)

    # Need a sum: start it at 0
    concatentations_sum = 0
    # "every possible a[i] and a[j]" --> 2 indices, or 2 nested for loops
    # iterate over the array
    # for each index front_index:
    for front_index in range(len(a)):
        # front_index is the index of the first element (front of the concatenation)
        # visit every other index to hit the possible combinations
        # for each front_index, we want to visit _every_ j / back_index (even if j == i, or j < i)
        for back_index in range(len(a)):
            # back_index is the index of the second / back of the concatenation
            # how do we concatenate?
            # we need to convert to strings using str
            # # str(a[front_index]), str(a[back_index])
            # front_string = str(a[front_index])
            # back_string = str(a[back_index])
            # concatenate the strings using +
            concatenated_string = str(front_string) + str(back_string)
            # convert back to int using int()
            concatenated_int = int(concatenated_string)
            # add the result of ^ to sum
            concatentations_sum += concatenated_int

    return concatentations_sum
    #


test_cases = [
    ([10, 2], 1344),
    ([8], 88),
    ([1, 2, 3], 198),
]

for input, output in test_cases:
    print(f"For input: {input} expecting {output}")
    actual_output = concatenationsSum(input)
    print(f"Actual output: {actual_output}")
    print("----")

# print(concatenationsSum(a))
