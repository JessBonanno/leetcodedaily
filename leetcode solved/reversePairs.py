
"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""


def reversePairs(nums):
    # EDGE CASE if the array length is less than 2 return 0
    if len(nums) < 2:
        return 0
    # init i to 0 and j to 1
    i = 0
    j = 1
    # init count for reverse pairs found
    count = 0
    # iterate the array
    while i <= len(nums) - 1:
        # check if i is less than j AND nums[i] is greater than 2 * nums[j]
        if i < j and nums[i] > 2 * nums[j]:
            # if so increment the count
            count += 1
        # when j reaches the end
        if j == len(nums) - 1:
            # increment i
            i += 1
            # reset j
            j = 0
        else:
            # else just increment j
            j += 1
    # return count of pairs found
    return count


nums = [1, 3, 2, 3, 1]
# print(f'reversePairs(nums): {reversePairs(nums)}')
