"""
164. Maximum Gap
Hard
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""

nums = [3, 6, 9, 1]


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    ordered = sorted(nums)
    largestDiff = 0
    for i in range(len(ordered) - 1):
        diff = ordered[i + 1] - ordered[i]
        if diff > largestDiff:
            largestDiff = diff
    return largestDiff


# print(maximumGap(nums))

