# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # A node is good if its value is >= the maximum value seen along the path
            is_good = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)
            
            # Recurse for left and right subtrees
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)
        
        return dfs(root, root.val)

        