"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    bfs 
    1. (same parent) for left childs, connect next to the right child
    2. (different parent) for right childs, connect next to parent's next's left child
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        # start with the root node, no next pointers
        leftmost = root

        # traversing level by level
        while leftmost.left:
            head = leftmost

            # traversing within a level, basic linked list traversal
            while head:

                # connection type 1
                head.left.next = head.right

                # connection type 2
                if head.next:
                    head.right.next = head.next.left

                head = head.next # next along the nodes on the same level
            leftmost = leftmost.left # go next level

        return root


        