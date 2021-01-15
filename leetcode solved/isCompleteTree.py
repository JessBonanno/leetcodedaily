
"""
958. Check Completeness of a Binary Tree
Medium

1072

14

Add to List

Share
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # we want to check each node for a right child
        # if a right child exists and no left child exists we can return false
        # if the left subtree is missing one or both children where the right
        # subtree at that level has children return false

        # init case where a node has no right child
        no_right_child = False
        # init case where a node has no children
        no_children = False
        # init queue for unexamined nodes
        queue = []
        # add root to queue
        queue.append(root)
        # breadth first search
        while len(queue) != 0:
            # current node to examine is taken from front of queue
            cur = queue.pop(0)
            # if we have already examined a node with no children or a left
            # child with no right child
            if no_right_child == True or no_children == True:
                # if current node has no left child return False
                if cur.left is not None:
                    return False
            # if the current node has no right child and has a left child
            if cur.right is None and cur.left is not None:
                # mark no right child as true
                no_right_child = True
                # add left child to queue if it exists
                if cur.left is not None:
                    queue.append(cur.left)
                # add right child to queue if it exists
                if cur.right is not None:
                    queue.append(cur.right)
            # if current node has no children
            if cur.right is None and cur.left is None:
                # mark no children as true
                no_children = True
                # add left child to queue if it exists
                if cur.left is not None:
                    queue.append(cur.left)
                # add right child to queue if it exists
                if cur.right is not None:
                    queue.append(cur.right)
            # if current node has a right child but no left child
            if cur.right is not None and cur.left is None:
                # return false
                return False
            # else append children to the queue if they exist
            else:
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
        # if we come out of the while loop never reaching false we can return
        # true
        return True

