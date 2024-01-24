"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
traverse from head looking for child nodes
merge a child into the parent list by:
1. connecting last node in child LL to next node in parent LL
2. connecting curr node in parent LL to first node in child LL
"""
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # function that moves the pointers to merge a child into the LL
        def merge(curr):

            child = curr.child # get the head of the child LL

            # traverse to the end of the child LL
            while child.next:
                child = child.next
            
            # link the end of child LL to the next node in the parent LL
            if curr.next:
                child.next = curr.next
                curr.next.prev = child

            # link the current node to the begninning of the child LL
            curr.next = curr.child
            curr.child.prev = curr

            curr.child = None # child pointers set to null
            
        curr = head
        while curr:
            if curr.child: # check for child node
                merge(curr) # if child node, merge into parent LL

            curr = curr.next # move to next node

        return head
        