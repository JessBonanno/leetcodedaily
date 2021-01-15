"""
*** First Duplicate ***
-----------------------
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.
"""

arr = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
# O(n^2) solution
# def firstDuplicate(a):
#     # keep track of matched index
#     matched = []
#     if len(a) < 2:
#         return -1
#     # iterate the list checking for duplicates of current number
#     for i, value in enumerate(a):
#         for j, val in enumerate(a):
#             if matched and matched[0] < i:
#                 continue
#             if j == i:
#                 continue
#             # if duplicate
#             if value == val:
#                 # if matched is empty just add the matched index
#                 if not matched:
#                     matched.append(j)
#                 # else check if theres a match with a larger index
#                 else:
#                     if matched[0] > j:
#                         # print('matched', matched, 'a', a[i])
#                         # if so replace it with the smaller index
#                         matched[0] = j
#     # if no matches return -1
#     if not matched:
#         return -1
#     else:
#         # there is a smallest match index return the value at that index
#         return a[matched[0]]
#
#
# print(firstDuplicate(arr))

arr = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]


# O(n) solution
def firstDuplicate(a):
    # define a set to hold non duplicate numbers
    nums = set()
    for i in range(len(a)):
        # if we hit a number that's duplicate (exists in the set) return it
        if a[i] in nums:
            return a[i]
        else:
            # else if its not duplicate add it to the set
            nums.add(a[i])
    # return -1 if no duplicates
    return -1


# print(firstDuplicate(arr))
