# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        def dfs(root):
            if root is None:
                return True, 0
            left_is_bal, left_depth = dfs(root.left)
            right_is_bal, right_depth = dfs(root.right)
            if not (left_is_bal and right_is_bal):
                return False, 0
            is_bal = bool(abs(right_depth - left_depth) <= 1)
            return is_bal, max(left_depth, right_depth) + 1

        return dfs(pRoot)[0]
