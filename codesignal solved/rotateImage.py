"""
*** Rotate image ***
--------------------
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""

a = [[1, 2, 3],  # 1 -> [0 : len - 1] 2 -> [1 : len - 1] 3 -> [2 : len -1]
     [4, 5, 6],  # 4 -> [0 : len - 2] 2 -> [1 : len - 2] 6 [2 : len -2]
     [7, 8, 9]]  # 7 -> [0 : len - 3] 8 -> [1 : len - 3] 9 -> [2 : len -3]


def rotateImage(a):
    # initialized the length of a set at 0
    length = len(a[0])
    # iterate through the length // 2
    for idx1 in range(length // 2):
        print(f'idx1, {idx1}')
        # starting from idx1, iterate (num3) over length idx1 -1 -  (should get 1)
        for idx2 in range(idx1, length - idx1 - 1):
            print(f'idx2, {idx2}')
            # initialize a placeholder
            holder = a[idx1][idx2]
            print(f'holder, {holder}')
            # replace the item at the cur_index of  a[idx1][idx2], with the item 90 degrees before              it
            a[idx1][idx2] = a[length - 1 - idx2][idx1]
            # replace the item moved with the item 90 degrees before it
            a[length - 1 - idx2][idx1] = a[length - 1 - idx1][length - 1 - idx2]
            # replace the item moved with the item 90 degrees before it
            a[length - 1 - idx1][length - 1 - idx2] = a[idx2][length - 1 - idx1]
            # replace the item moved with the item 90 degrees before it, which is the holder
            a[idx2][length - 1 - idx1] = holder
    return a


# with zip
# def rotateImage(a):
#     return list(zip(*reversed(a)))

# with comprehension
# def rotateImage(a):
#     return [[x[i] for x in a][::-1] for i in range(len(a))]


# print(rotateImage(a))
