class Solution:
    def flatten(self, head: 'Node', next_=None) -> 'Node':
        
        curr, prev = head, None

        # traverse LL
        while curr:
            # has child LL
            if curr.child:
            
                tail = curr.next # the node which the child LL connects to

                # recurse for child LL
                curr.next = self.flatten(curr.child, tail)

                # linking first node in child LL to node in parent LL
                if curr.next: 
                    curr.next.prev = curr

                curr.child = None

            prev = curr
            curr = curr.next

        # linking last node in child LL to next node in parent LL
        if prev:  
            prev.next = next_
        if next_: 
            next_.prev = prev

        return head