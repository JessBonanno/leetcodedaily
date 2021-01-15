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
        #  at this point we have the entire current path
        else:
            # if the current path is a directory ( not '.' or '..' or empty string)
            if cur_path != ".." and cur_path != "." and cur_path != "":
                # add the current path to the list of paths
                path_arr.append(cur_path)
                # reset the current path
                cur_path = ""
            # if the current path is '..' pop off the top of the stack as long
            # the stack is not empty
            elif cur_path == ".." and len(path_arr) != 0:
                path_arr.pop()
                # reset the current path
                cur_path = ""
            cur_path = ""
    # initialize an empty string to hold our result
    result = "/"
    # iterate the list of paths
    for i in range(len(path_arr)):
        # if we are not at the last path in the list
        if i != len(path_arr) - 1:
            # add the path followed by '/' to the result
            result += path_arr[i] + "/"
        # if we are at the last path
        else:
            # only add the path without the trailing '/'
            result += path_arr[i]
    # return the result
    return result


# print(f'simplifyPath(path = "/home/a/./x/../b//c/"): {simplifyPath(path)}')
