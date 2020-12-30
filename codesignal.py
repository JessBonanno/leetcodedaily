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

"""
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
Example
For n = 240, the output should be
lateRide(n) = 4.
Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
For n = 808, the output should be
lateRide(n) = 14.
808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
The duration of your ride, in minutes. It is guaranteed that you've been riding for less than a day (24 hours).
Guaranteed constraints:
0 ≤ n < 60 · 24.
[output] integer
The sum of the digits the digital timer would show.
"""

n = 808


def lateRide(n):
    # init result
    result = 0
    # init hour equal to n // 60 in string format
    hour = str(n // 60)
    # for every digit in hour
    for digit in hour:
        # convert it back to an int and add it to the result
        result += int(digit)
    # init mins equal to ( n - hour in int format * 60 ) in string format
    mins = str(n - (int(hour) * 60))
    # for every digit in mins
    for digit in mins:
        # convert it back to an int and add it to the result
        result += int(digit)
    return result


print(f'lateRide(808): {lateRide(n)}')

"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
Example
For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
Guaranteed constraints:
1 ≤ n < 104.
[output] integer
The area of the n-interesting polygon.
"""

n = 3


def shapeArea(n):
    # the area is equal to n squared + (n - 1) squared
    return n ** 2 + (n - 1) ** 2


print(f'shapeArea(3): {shapeArea(n)}')

"""
Note: Avoid using built-in std::nth_element (or analogous built-in functions in languages other than C++) when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.
Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.
Example
For nums = [7, 6, 5, 4, 3, 2, 1] and k = 2, the output should be
kthLargestElement(nums, k) = 6;
For nums = [99, 99] and k = 1, the output should be
kthLargestElement(nums, k) = 99.
Input/Output
[execution time limit] 4 seconds (py3)
[input] array.integer nums
Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-105 ≤ nums[i] ≤ 105.
[input] integer k
Guaranteed constraints:
1 ≤ k ≤ nums.length.
"""

nums = [7, 6, 5, 4, 3, 2, 1]
k = 2


def kthLargestElement(nums, k):
    # sort the array in descending order
    sorted_nums = sorted(nums, reverse=True)
    # iterate the sorted array
    for i in range(len(sorted_nums)):
        # when we reach k - 1 we have our result because of zero based index
        if i == k - 1:
            return sorted_nums[i]


print(
    f'kthLargestElement(nums = [7, 6, 5, 4, 3, 2, 1], k = 2): {kthLargestElement(nums, k)}')

"""
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
Here is some info on Unix file system paths:
/ is the root directory; the path should always start with it even if it isn't there in the given path;
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
this also means that // stands for "change the current directory to the current directory"
. is used to mark the current directory;
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.
Example
For path = "/home/a/./x/../b//c/", the output should be
simplifyPath(path) = "/home/a/b/c".
Here is how this path was simplified:
* /./ means "move to the current directory" and can be replaced with a single /;
* /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
* // means "move to the current directory" and can be replaced with a single /.
Input/Output
[execution time limit] 4 seconds (py3)
[input] string path
A line containing a path presented in Unix style format. All directories in the path are guaranteed to consist only of English letters.
Guaranteed constraints:
1 ≤ path.length ≤ 5 · 104.
"""

path = "/home/a/./x/../b//c/"


def simplifyPath(path):
    # EDGE CASE if path is '/' just return it
    if path == "/":
        return path
    # standardizing all paths to end with '/'
    if path[len(path) - 1] != "/":
        path += "/"
    # standardizing all paths to start with '/'
    if path[0] != "/":
        path = "/" + path
    # init cur path to hold path we are processing
    cur_path = ""
    # init array to hold each path
    path_arr = []

    # iterate the length of the path
    for i in range(1, len(path)):
        # if the current character is not '/'
        if path[i] != "/":
            # add the current character to the current path
            cur_path += path[i]
        else:
            # if the current character is '/' we can add the current path to
            # the path array and reset the current path to ''
            path_arr.append(cur_path)
            cur_path = ""
    # init array to hold paths without './'
    cleaned_paths = []
    # iterate the path_arr
    for i in range(len(path_arr)):
        # if the current character is not '.'
        if path_arr[i] != ".":
            # add the path to the cleaned paths array
            cleaned_paths.append(path_arr[i])
    # init array to hold the final paths
    final_paths = []
    # iterate the cleaned paths
    for i in range(len(cleaned_paths)):
        # if the current path is not '..'
        if cleaned_paths[i] != "..":
            # add it to the final paths array
            final_paths.append(cleaned_paths[i])
        else:
            # else if the current path IS '..' and the length of final paths
            # is not 0
            if len(final_paths) != 0:
                # we can pop the last path added off of the final paths array
                final_paths.pop()

    # init result string to hold our final result
    result = ""
    # for each directory in final paths array
    for dir in final_paths:
        # if the dir is not an empty string
        if dir != "":
            # add it to the result prepended with a '/'
            result += ("/" + dir)
    # if the result is an empty string
    if result == "":
        # return '/'
        return "/"
    # return the result string
    return result


print(f'simplifyPath(path = "/home/a/./x/../b//c/"): {simplifyPath(path)}')
