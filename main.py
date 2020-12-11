"""
Daily Leetcode practice
"""

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


"""
1304. Find N Unique Integers Sum up to Zero
Easy

426

255

Add to List

Share
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
"""

n = 5
import random


def sumZero(n):
    # Initial try less efficient
    # result = []
    # sum = 0
    # for i in range(n - 1):
    #     num = random.randint(0, n * 10)
    #     while num in result:
    #         num = random.randint(0, n * 10)
    #     result.append(num)
    #     sum += num
    #
    # result.append(-sum)
    # return result

    # much more efficient by cutting the loop in 1/2
    count = 1000
    res = []
    i = n
    while i >= 2:
        i -= 2
        res.append(count)
        res.append(count * -1)
        count -= 1

    if i == 1:
        res.append(0)
    return res


print(sumZero(n))
