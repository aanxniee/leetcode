"""
REQUIREMENTS:
1. store a key-value pair
2. update a key-value pair
3. find value given a key, if it doesn't exist return -1
4. create new node for new key-value pair, put at end
5. when an existing key is updated or fetched, find its associated linked list node and move it to the end
6. when a key-value pair is added and the size > capacity, remove the node at the front

NOTES:
1-3 can be achieved with hashmap
4-6 can be achieved keeping head and tail ptrs to the linkedlist
5 map key to node (int: ListNode), to access value, use node.val

EDGE CASES:
empty list case, deleting only node means deleting head and tail
can fix this using sentinel nodes (don't hold any data)
real head is head.next and real tail is tail.prev
prevents head or tail to be null
"""

"""
each node represents an element in the data structure, storing key-value pair in each node. using a double linked list for o(1) insertion and deletion. most used is near the tail, least used is near the head
"""
class ListNode:
    def __init__(self, key: int, val: int):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict() # store key:node pairs

        # sentinel head and tails
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        # connect the head and tails together
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        # if the key is not found, return -1
        if key not in self.dic:
            return -1

        node = self.dic[key] # retrieve node from dict
        # remove it from its position and store at the end (was recently used)
        self.remove(node)
        self.add(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        # if key-value pair was already added before, delete it (to move it to the end, recently used)
        if key in self.dic:
            oldNode = self.dic[key]
            self.remove(oldNode)

        # create new linked list node and also add to dict
        node = ListNode(key, value)
        self.add(node)
        self.dic[key] = node

        # exceeds capacity, remove node near the head and remove from dict
        if len(self.dic) > self.capacity:
            deleteNode = self.head.next
            self.remove(deleteNode)
            del self.dic[deleteNode.key]

    # adds node to the end
    def add(self, node):
        previous = self.tail.prev
        previous.next = node
        node.prev = previous
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)