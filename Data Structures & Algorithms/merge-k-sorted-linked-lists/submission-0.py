import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        min_heap = []
        
        for l in lists:
            if l:
                heapq.heappush(min_heap, l)
                
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(min_heap, node.next)
                
        return dummy.next