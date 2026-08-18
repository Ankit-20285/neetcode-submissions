"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map original nodes to their cloned counterparts
        old_to_new = {}

        # Pass 1: Create all new nodes without wiring connections
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Connect next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]