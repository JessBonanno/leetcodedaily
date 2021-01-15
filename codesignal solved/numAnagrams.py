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

