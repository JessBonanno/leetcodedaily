"""
Mutate the array
----------------
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1]
"""
a = [4, 0, 1, -2, 3]
n = 5


# passing
def mutateTheArray(n, a):
    if len(a) < 2:
        return a
    result = []
    for i in range(len(a)):
        # if i = 0 then i - 1 does not exist so [i-1] becomes 0 and we can
        # just leave it off
        if i == 0:
            result.append(a[i] + a[i + 1])
        # if i is pointing to the last element then [i + 1] does not exist so
        # it becomes 0 and we can just leave that off
        elif i == len(a) - 1:
            result.append((a[i - 1] + a[i]))
        # for all other cases just do the normal equation
        else:
            result.append(a[i - 1] + a[i] + a[i + 1])

    return result


# print(mutateTheArray(n, a))
