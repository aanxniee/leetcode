"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return

        q = [root]

        while q:
            r = None

            for i in range(len(q)):
                curr = q.pop(0)

                curr.next = r
                r = curr

                if curr.right:
                    q.append(curr.right)

                if curr.left:
                    q.append(curr.left)

        return root