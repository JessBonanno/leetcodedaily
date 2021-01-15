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
