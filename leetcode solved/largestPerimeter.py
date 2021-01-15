"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
"""


def largestPerimeter(A):
    # the sum of two side lengths of a triangle is always greater than the third side. If this is true     for all three combinations of added side lengths
    # sort the array from largest to smallest so as soon as we find a
    # perimeter we can stop running the function
    A = sorted(A, reverse=True)

    # helper function to get the perimeter of the triangle if it exists
    def getPerimeter(arr):
        if arr[0] + arr[1] > arr[2]:
            if arr[1] + arr[2] > arr[0]:
                if arr[0] + arr[2] > arr[1]:
                    return arr[0] + arr[1] + arr[2]
        return 0

    # iterate the array grabbing 3 numbers at a time and call getPerimeter
    # function
    for i in range(len(A) - 2):
        nums_to_check = A[i:i + 3]
        current_perimeter = getPerimeter(nums_to_check)
        # if the function returns a perimeter we can just stop and return it
        if current_perimeter > 0:
            return current_perimeter
    # if we never find a perimeter we return 0
    return 0


A = [1, 4, 18, 3, 8, 4, 4]
print(f'largestPerimeter: {largestPerimeter(A)}')
