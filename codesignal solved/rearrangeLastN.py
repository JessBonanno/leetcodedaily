"""
Rearrange Last N
----------------
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l is None:
        return l
    if n == 0:
        return l
    if l.next is None:
        return l
    # set a current, a head, a previous
    new_head = None
    cur = l
    new_last_node = None
    # var to hold length of list
    length = 0
    # get the length of the list by traversing
    while cur is not None:
        cur = cur.next
        length += 1
    # take the last node in the list and point it to the first node in the list
    if n == length:
        return l
    # reinitialize current to l
    cur = l
    for i in range(length):

        # length -n - 1 ( item before the group to move to the head) needs to point to none
        if i == length - n - 1:
            new_head = cur.next
            new_last_node = cur

            # cur = cur.next

        # length - n is the new head
        # if i == length - n:
        #     pass
        # take the last node in the list and point it to the first node in the list
        if i == length - 1:
            cur.next = l
        if cur:
            cur = cur.next

    new_last_node.next = None
    cur = new_head
    return new_head
