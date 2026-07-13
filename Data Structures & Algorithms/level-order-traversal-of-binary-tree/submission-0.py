from collections import deque 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        queue = deque([root])
        ans = []

        while queue: 
            level_length = len(queue)
            current = []

            for _ in range(level_length): 
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                current.append(node.val)

            ans.append(current)
        
        return ans