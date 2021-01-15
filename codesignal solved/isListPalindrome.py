
"""
*** Is list palindrome ***
--------------------------
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# my solution (used google)
def isListPalindrome(l):
    if l is None:
        return True
    head = l
    prev = None
    while l.next:
        l.prev = prev
        prev = l
        l = l.next
    tail = l
    tail.prev = prev
    while head is not tail and head.value == tail.value:
        head = head.next
        tail = tail.prev
    if head is tail:
        return True
    elif head.value == tail.value:
        return True
    else:
        return False


# best voted on codesignal
# def isListPalindrome(l):
#     if not l or not l.next:
#         return True
#     s = 1
#     n = l
#     while n.next:
#         n = n.next
#         s += 1
#
#     middle = s // 2
#
#     n = l
#     for i in range(middle):
#         n = n.next
#
#     if s % 2:
#         n = n.next
#
#     r = n  # reverse n
#     m = r.next
#     for _ in range(middle - 1):  # flip n
#         m.next, r, m = r, m, m.next
#
#     for _ in range(middle):
#         if r.value != l.value:
#             return False
#         r = r.next
#         l = l.next
#
#     return True
