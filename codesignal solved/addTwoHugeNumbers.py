"""
*** Add two huge numbers
------------------------
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.
"""


# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


a = [1]
b = [9999, 9999, 9999, 9999, 9999, 9999]


# my code couldn't get to pass
# def addTwoHugeNumbers(a, b):
#     if a is None and b is None:
#         return [0]
#     if a.value == 0:
#         return b
#
#     cur_a = a
#     cur_b = b
#     a_val = ''
#     b_val = ''
#     a_count = len(str(a.value))
#     b_count = len(str(b.value))
#     count = max(a_count, b_count)
#     print('count:', count)
#     while cur_a is not None:
#         zeros = count - len(str(cur_a.value))
#         a_val += '0'*zeros
#         a_val += str(cur_a.value)
#         cur_a = cur_a.next
#
#     while cur_b is not None:
#         b_val += str(cur_b.value)
#         cur_b = cur_b.next
#
#     result = str(int(a_val) + int(b_val))
#     print('a:', a_val)
#     print('b:', b_val)
#     print(result)
#     n = count
#
#     res_arr = [int(result[i:i+n]) for i in range(0, len(result), n)]
#     print('res arr', res_arr)
#     for num in res_arr:
#         if num > 0:
#             num = int(str(num).rstrip('0'))
#         if len(str(a[0])) == 1:
#             num = int(str(num).rstrip('0'))
#
#     return res_arr
#
# print(addTwoHugeNumbers(a, b))


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# top codesignal passing solution
def addTwoHugeNumbers(a, b):
    a = reverse(a)
    b = reverse(b)

    carry = 0
    result = None

    while a is not None or b is not None or carry > 0:
        raw = ((a.value if a is not None else 0) +
               (b.value if b is not None else 0) +
               carry)

        node = ListNode(raw % 10000)
        node.next = result

        result = node
        carry = raw // 10000

        if a is not None:
            a = a.next
        if b is not None:
            b = b.next

    return result


def reverse(list):
    current = list
    previous = None

    while current is not None:
        previous, current.next, current = current, previous, current.next

    return previous

