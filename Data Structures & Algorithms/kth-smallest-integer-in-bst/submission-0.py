# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None

        def dfs(node):
            if not node or self.answer is not None:
                return

            dfs(node.left)

            self.count += 1

            if self.count == k:
                self.answer = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.answer