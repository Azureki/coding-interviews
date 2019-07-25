# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre: return None
        i = tin.index(pre[0])
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:1 + i], tin[:i])
        root.right = self.reConstructBinaryTree(pre[1 + i:], tin[i + 1:])
        return root

