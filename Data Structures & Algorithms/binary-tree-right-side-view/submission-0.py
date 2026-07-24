from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = deque([root])
        answer = []

        while queue: 
            level_size = len(queue)

            for i in range(level_size): 
                node = queue.popleft()
                # if level_size == 1: 
                #     answer.append(node.val)
                
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == (level_size - 1): 
                    answer.append(node.val)
        
        return answer