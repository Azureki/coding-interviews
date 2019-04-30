from queue import Queue


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        q = Queue()
        q.put(root)
        while not q.empty():
            mask = q.get()
            res.append(mask.val)
            if mask.left:
                q.put(mask.left)
            if mask.right:
                q.put(mask.right)
        return res


root = TreeNode(1)
res = Solution().PrintFromTopToBottom(root)
print(res)
