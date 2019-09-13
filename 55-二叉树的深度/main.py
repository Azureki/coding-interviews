# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        def dfs(root):
            if root is None:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            return max(left_depth, right_depth) + 1
        return dfs(pRoot)
